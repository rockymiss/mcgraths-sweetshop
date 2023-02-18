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

    search_fields = ['name', 'description']
    list_display = ('name',
                    'category',
                    'product_price',
                    'description',
                    'image_url',
                    'product_image',
                    'status')
    
    ordering = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Registers the Category Model in admin so that categories 
    can be added, removed or amended easily.  Applies search fields 
    and what fields are displayed
    """

    search_fields = ['name']
    list_display = ('name',
                    'cat_friendly_name')
