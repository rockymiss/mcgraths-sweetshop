from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from .models import Products


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

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__in=categories)
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

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/all_products.html', context)


# class ProductList(ListView):
#     """
#     Displays a list of all products and provides a 
#     search functionality to display products that the 
#     user has searched for
#     """
#     model = Products
#     template_name = 'products/all_products.html'
#     queryset = Products.objects.all()

#     def get_queryset(self):
#         """
#         Overrides queryset and allows user to search
#         by name or description of product
#         """
#         query = self.request.GET.get('q')
#         category = self.request.GET.get('category')

#         if category:
#             object_list = self.model.objects.filter(
#                 Q(category__icontains=category) 
#             )

#         if query:
#             object_list = self.model.objects.filter(
#                 Q(product_name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         else:
#             object_list = Products.objects.all()

#         return object_list


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
