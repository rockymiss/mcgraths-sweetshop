"""
urls for contact app
"""
from django.urls import path
from .views import ContactCreate, Confirm, ReviewMessage, DeleteMessage

urlpatterns = [
    path('contact/', ContactCreate.as_view(), name="contact"),
    path('confirm_message/', Confirm.as_view(), name="confirm_message"),
    path('review_message/', ReviewMessage.as_view(), name="review_message"),
    path('delete_message/<int:pk>/',
         DeleteMessage.as_view(), name="delete_message"),
]
