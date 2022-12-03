from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from .models import Products


class ProductList(ListView):
    """
    Displays a list of all products and provides a 
    search functionality to display products that the 
    user has searched for
    """
    model = Products
    template_name = 'products/all_products.html'
    queryset = Products.objects.all()

    def get_queryset(self):
        """
        Overrides queryset and allows user to search
        by name or description of product
        """
        query = self.request.GET.get('q')

        if query:
            object_list = self.model.objects.filter(
                Q(product_name__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            object_list = Products.objects.all()

        return object_list


class ProductDetail(View):
    """
    Displays the product on it's own that the user selects 
    from the Product list.
    """

    def get(self, request, pk, *args, **kwargs):
        """
        gets the objects instance's and assigns primary key
        """
        product = get_object_or_404(Products, pk=pk)
        context = {
            'product': product,
        }

        return render(
            request,
            "products/product_detail.html",
            context
            )
