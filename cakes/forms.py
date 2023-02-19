from django import forms
from .models import CakePost, CakeComment


class CreateCake(forms.ModelForm):
    """
    A Form to allow a user to create a cake
    post
    """
    class Meta:
        model = CakePost

        fields = ('full_name',
                  'title',
                  'cake_image',
                  'description',
                  'status',)
        prepopulated_fields = {'slug': ('title',)}


class CreateComment(forms.ModelForm):
    """
    A form to allow a user to leave comments on a cake post
    """
    class Meta:
        model = CakeComment
        fields = ('comment_body',)
