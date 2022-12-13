from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(product_price, quantity):
    return product_price * quantity
