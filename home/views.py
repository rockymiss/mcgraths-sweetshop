from django.shortcuts import render
from django.views.generic import TemplateView

# Template Views


class HomePageView(TemplateView):
    """
    Creates view for the Home Page
    """
    template_name = "home/index.html"
