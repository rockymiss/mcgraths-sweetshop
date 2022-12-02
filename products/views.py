from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import generic, View
from .models import Products


class ProductList(generic.ListView):
    """
    Creates a list of blogs with status of posted
    using the BlogPost Model
    """
    model = Products
    queryset = Products.objects.order_by('product_name')
    template_name = 'products/all_products.html'
    context_object_name = "products"


class ProductDetail(View):
    """
    This class will display the product the user selects from
    the Product list.
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
