"""Forms for Contact"""

from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):
    """
    Form for user to contact owner
    """
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'message'
        ]
        widgets = {
            'message': Textarea(
                attrs={
                    "placeholder": "We would love to hear from you"
                }
            )
        }
