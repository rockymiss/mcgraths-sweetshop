"""mcgraths_shop URL Configuration"""

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
]