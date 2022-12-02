"""mcrocks URL Configuration"""

from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view(), name="products"),
    path('products/<int:pk>', views.ProductDetail.as_view(), name="product_detail")
]
