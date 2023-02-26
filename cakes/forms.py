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
                  'cake_approve',)
        prepopulated_fields = {'slug': ('title',)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cake_approve'].initial = False
        self.fields['cake_approve'].widget = forms.HiddenInput()


class CreateComment(forms.ModelForm):
    """
    A form to allow a user to leave comments on a cake post
    """
    class Meta:
        model = CakeComment
        fields = ('comment_body',)
