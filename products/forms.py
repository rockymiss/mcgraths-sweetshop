from django import forms
from .widgets import CustomClearableFileInput
from .models import Products, Category


class ProductForm(forms.ModelForm):
    """
    Form for superuser to update stock
    """

    class Meta:
        model = Products
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'
                                            ] = 'border-black rounded-0'
