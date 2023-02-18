from django.db import models
from cloudinary.models import CloudinaryField

DISCOUNT = ((0, "DiscountNo"), (1, "DiscountYes"))


class Category(models.Model):
    """ Category model for products """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=240)
    cat_friendly_name = models.CharField(max_length=240, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_cat_friendly_name(self):
        return self.cat_friendly_name


class Products(models.Model):
    """ Model for Products that will be sold """
    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=240)
    description = models.TextField()
    has_colours = models.BooleanField(default=False, null=True, blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.IntegerField(choices=DISCOUNT, default="0")
    product_image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(max_length=1050, null=True, blank=True)

    def __str__(self):
        return self.name
