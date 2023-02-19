""" Admin Panel for Cakes"""

from django.contrib import admin
from .models import CakePost, CakeComment

# Register your models here.


@admin.register(CakePost)
class CakeAdmin(admin.ModelAdmin):
    """
    Applies display, filter and search to the CakePost Model
    """
    search_fields = ['title', 'description']
    list_display = ('title',
                    'slug',
                    'status',
                    'date_created',
                    'full_name')
    list_filter = ('status', 'date_created')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CakeComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Applies display, filter, search and action functionality
    to the Comment Model on the admin panel
    """
    list_display = ('name',
                    'comment_created',
                    'comment_body',
                    'comment_approve')
    list_filter = ('comment_approve', 'comment_created')
    search_fields = ('name', 'comment_body')
    actions = ['comment_approve']

    def comment_approve(self, queryset):
        """
        Creates an action which allows admin to approve a comment
        """
        queryset.update(comment_approve=True)
