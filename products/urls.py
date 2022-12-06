"""mcrocks URL Configuration"""

from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list, name="products"),
    path('<product_id>', views.ProductDetail.as_view(), name="product_detail"),
]
