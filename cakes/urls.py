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
     path('cake_review/', views.ReviewCakePost.as_view(), name='cake_review'),
     path('cake_approve/<int:pk>/',
          views.ApproveCake.as_view(), name="cake_approve"),
     path('cake_delete/<int:pk>/',
          views.DeleteCake.as_view(), name="cake_delete")
]
