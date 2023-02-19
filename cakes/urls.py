"""
urls for cakes app
"""
from django.urls import path
from . import views


urlpatterns = [

    path('cakes/', views.CakeList.as_view(), name='cakes'),
    path('cake_detail/<slug:slug>/',
         views.CakeDetail.as_view(), name="cake_detail"),
    path('favourite/<slug:slug>/',
         views.Favourites.as_view(), name="favourite"),
    path('create_cake/', views.CreateCakeView.as_view(), name='create_cake'),
]
