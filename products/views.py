from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
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
