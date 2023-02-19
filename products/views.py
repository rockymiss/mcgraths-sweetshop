from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import DetailView, TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic, View

from django.db.models.functions import Lower

from .models import Products, Category
from .forms import ProductForm


def product_list(request):
    """
    Displays a list of all products, provides a
    search functionality to display products that the
    user has searched for and provides a way for the user
    to filter by some categories.  Followed Boutique Ado

    """

    products = Products.objects.all()
    product_drop = Products.objects.all()
    query = None
    categories = None
    offers = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'status' in request.GET:
            offers = request.GET['status']
            products = products.filter(status=1)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(request, "Why didn't you search for anything?")
                return redirect(reverse('products'))

            query = Q(
                name__icontains=query
                ) | Q(description__icontains=query)
            products = products.filter(query)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'offers': offers,
        'product_drop': product_drop,

    }

    return render(request, 'products/all_products.html', context)


class ProductDetail(View):
    """
    Displays the product on it's own that the user selects 
    from the Product list.
    """

    def get(self, request, product_id):
        """
        gets the objects instance's and assigns primary key
        """
        product = get_object_or_404(Products, pk=product_id)
        context = {
            'product': product,
        }

        return render(
            request,
            "products/product_detail.html",
            context
            )

@login_required
def add_product(request):
    """
    Add a product to the shop
    """
    if not request.user.is_superuser:
        messages.error(
                       request,
                       'Sorry, only store owners can access this page')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product, Check the Form')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Add a product to the shop
    """
    if not request.user.is_superuser:
        messages.error(
                       request,
                       'Sorry, only store owners can access this page')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the shop """

    if not request.user.is_superuser:
        messages.error(
                       request,
                       'Sorry, only store owners can access this page')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


# Management Views

class ManagementCheck(TemplateView):
    """
    Creates view for Management Page
    """
    template_name = "products/management.html"
