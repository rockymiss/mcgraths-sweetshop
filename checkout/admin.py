from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    A class to allow admin to add and edit line items
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    A class to add read-only fields that will be calculated by
    the model methods, specifies the order of the fields in admin
    and a list display option to restrict the columns that 
    show in the order list.  Items will be ordered by date. 
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'address1',
              'address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)