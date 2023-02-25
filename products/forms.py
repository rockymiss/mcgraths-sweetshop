from django import forms
from .widgets import CustomClearableFileInput
from .models import Products, Category
import cloudinary


class ProductForm(forms.ModelForm):
    """
    Form for superuser to update stock
    """

    class Meta:
        model = Products
        fields = [
            'category',
            'name',
            'description',
            'has_colours',
            'product_price',
            'status',
            'product_image',
            'image_url',
            ]

    product_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id,
                           c.get_cat_friendly_name())
                          for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
