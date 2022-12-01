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
    Shows individual products on their own page
    """

    model = Products
    template_name = 'products/product_detail.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.id})
