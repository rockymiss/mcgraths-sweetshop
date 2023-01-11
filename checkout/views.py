from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.


def checkout(request):
    """
    Function to display the checkout form
    """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing to see here!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MP9NvK1vVL0oSYfi1s2vhoR5uWpXyIeky3LxrsCmegLva9hjkYVcFuFN2Tzc99ec5h1rwHXcGRVoNkYLUqCJI3m00p6SEJrwT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
