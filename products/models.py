from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category model for products """
    category_name = models.CharField(max_length=240)
    cat_friendly_name = models.CharField(max_length=240, null=True, blank=True)

    def __str__(self):
        return self.category_name
    
    def __stf__(self):
        return self.cat_friendly_name


class Products(models.Model):
    """ Model for Products that will be sold """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=240)
    product_image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1050, null=True, blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_sku = models.CharField(max_length=240, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.product_name
