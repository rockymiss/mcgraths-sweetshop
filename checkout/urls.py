"""checkout URL Configuration"""

from django.urls import path
from . import views
from .views import DiscountPage, CreateDiscountView
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/',
         views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('discounts/', DiscountPage.as_view(), name="discount_page"),
    path('checkout/discounts/',
         CreateDiscountView.as_view(), name="create_discount"),
    path('delete_discount/<int:pk>/',
         views.DeleteDiscount.as_view(), name="delete_discount"),
]
