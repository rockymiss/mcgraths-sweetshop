"""
Views for Contact App
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm


class ContactCreate(CreateView):
    """
    Creates a view so that users
    can fill out a contact form to
    contact the owners
    """
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("confirm_message")


class Confirm(TemplateView):
    """
    Creates view for a confirmation for the client
    """
    template_name = "confirm_message.html"


class ReviewMessage(UserPassesTestMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Messages made by user
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'review_message.html'
    model = Contact
    queryset = Contact.objects.order_by('date_created')
    context_object_name = 'review_message'


class DeleteMessage(UserPassesTestMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a message sent by the user
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's id and assigns primary key
        """
        review_message = get_object_or_404(Contact, pk=pk)
        context = {
            'review_message': review_message,
        }

        return render(
            request,
            'delete_message.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the message the user made then Admin can
        delete the message
        """

        review_message = get_object_or_404(Contact, pk=pk)
        review_message.delete()

        return redirect('review_message')
