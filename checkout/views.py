from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views import generic, View
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm, DiscountForm, AdminDiscount
from products.models import Products
from .models import Order, OrderLineItem, Discount

from user_profiles.forms import UserProfileForm
from user_profiles.models import UserProfile

from cart.contexts import cart_contents

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:

        messages.error(request, 'Sorry, your payment cannot be \
            processed right now.  Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Products.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for colour, quantity in (item_data['items_by_colour']
                                                 .items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_colour=colour,
                            )
                            order_line_item.save()
                except Products.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your bag wasn't found in \
                        our database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Check if a discount code has been submitted
            discount_applied = False
            if request.POST.get('user_discount_code'):
                discount_form = DiscountForm(request.POST)
                if discount_form.is_valid():
                    discount_code = discount_form.cleaned_data[
                            'user_discount_code']
                    try:
                        discount = Discount.objects.get(
                            discount_code=user_discount_code)
                    except Discount.DoesNotExist:
                        discount = None
                    if discount:
                        discount_applied = True
                        order.discount_code = discount
                        order.save()

            # Apply the discount if applicable
            if discount_applied:
                total = order.get_discount_total()
            else:
                total = order.grand_total
            order.save()

            # Clear the cart
            request.session['cart'] = {}

            # Redirect to the checkout success page
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'address1': profile.default_address1,
                    'address2': profile.default_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_address1': order.address1,
                'default_address2': order.address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    if 'user_discount_code' in request.session:
        del request.session['user_discount_code']

    if 'discount_percentage' in request.session:
        del request.session['discount_percentage']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


class DiscountPage(generic.ListView):
    """
    A simple view to see all discounts
    created by Admin
    """
    template_name = "checkout/view_discounts.html"
    model = Discount
    queryset = Discount.objects.all
    context_object_name = 'review_discounts'


class CreateDiscountView(LoginRequiredMixin, CreateView):
    """
    Allows a user or admin to create
    a testionial on the front end
    """
    template_name = 'checkout/create_discount.html'
    form_class = AdminDiscount

    def test_func(self):
        """
        Checks if user
        """
        return self.request.user.is_authenticated

    def get_success_url(self):
        """
        sets the reverse url when user
        or admin creates a new Discount
        """
        return reverse('discount_page')

    def form_valid(self, form):
        """
        Validates the form and adds the new discount to the
        view_discounts page
        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'You have added a new Discount Code!')
        return super().form_valid(form)


class DeleteDiscount(LoginRequiredMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a discount code
    """

    model = Discount
    success_url = reverse_lazy('discount_page')

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        delete_discount = get_object_or_404(Discount, pk=pk)
        context = {
            'delete_discount': delete_discount,
        }

        return render(
         request,
         'checkout/delete_discount.html',
         context)
