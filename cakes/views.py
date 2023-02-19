from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView
from django.views import generic, View
from .models import CakePost, CakeComment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify

# Create your views here.


class CakeList(generic.ListView):
    """
    Displays a list of Cake Posts with status of Posted
    using the CakePost Model
    """
    model = CakePost
    queryset = CakePost.objects.filter(status=1,
                                       cake_approve=True).order_by(
                                       '-date_created')
    template_name = 'cakes.html'
    context_object_name = "cakelist"
