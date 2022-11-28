from django.contrib import admin
from .models import Products, Category

# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """
    Registers the Product Model in admin so that products 
    can be added, removed or amended easily.  Applies search fields 
    and what fields are displayed
    """

    search_fields = ['product_name', 'description']
    list_display = ('product_name',
                    'category',
                    'description',
                    'product_price',
                    'product_image',
                    'image_url')
    
    ordering = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Registers the Category Model in admin so that categories 
    can be added, removed or amended easily.  Applies search fields 
    and what fields are displayed
    """

    search_fields = ['category_name']
    list_display = ('category_name',
                    'cat_friendly_name')
