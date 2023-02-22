from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products


def cart_contents(request):
    """
    A function to make the dictionary available to
    all templates
    """

    cart_items = []
    total = 0
    product_count = 0
    discount = Decimal('0.00')
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Products, pk=item_id)
            total += item_data * product.product_price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Products, pk=item_id)
            for colour, quantity in item_data['items_by_colour'].items():
                total += quantity * product.product_price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colour': colour,
                })
    
    # Check if discount code is applied 

    if 'user_discount_code' in request.session:
        discount_percent = Decimal(request.session['discount_percentage'])
        discount = (total * discount_percent) / 100
        total -= discount

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': float(total),
        'product_count': product_count,
        'delivery': float(delivery),
        'free_delivery_delta': float(free_delivery_delta),
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': float(grand_total),
        'discount': float(discount),
    }

    return context
