from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from .models import Products, Category
from django.db.models.functions import Lower


def product_list(request):
    """
    Displays a list of all products, provides a
    search functionality to display products that the
    user has searched for and provides a way for the user
    to filter by some categories.  Followed Boutique Ado

    """

    products = Products.objects.all()
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
                messages.error(request, "Why didn't you search for anything?")
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
