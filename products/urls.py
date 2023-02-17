"""mcrocks URL Configuration"""

from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list, name="products"),
    path('<int:product_id>/', views.ProductDetail.as_view(),
         name="product_detail"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
]
