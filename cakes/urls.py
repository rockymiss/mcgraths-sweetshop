"""
urls for cakes app
"""
from django.urls import path
from . import views


urlpatterns = [

    path('cakes/', views.CakeList.as_view(), name='cakes'),
    path('cake_detail/<slug:slug>/',
         views.CakeDetail.as_view(), name="cake_detail"),
]
