from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Products

# Create your views here.


def view_cart(request):
    """
    Returns the shopping cart view
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Adds a quantity of the item the user selects to the Cart
    Also allows the user to tore the contents of the Cart when 
    browsing the website elsewhere
    """
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None

    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    cart = request.session.get('cart', {})

    if colour:
        if item_id in list(cart.keys()):
            if colour in cart[item_id]['items_by_colour'].keys():
                cart[item_id]['items_by_colour'][colour] += quantity
                messages.success(request, f'You added {cart[item_id]["items_by_colour"][colour]} {product.name} with the colour {colour.upper()} to your cart')
            else:
                cart[item_id]['items_by_colour'][colour] = quantity
                messages.success(request, f'You added {product.name} with the colour {colour.upper()} to your cart ')
        else:
            cart[item_id] = {'items_by_colour': {colour: quantity}}
            messages.success(request, f'You added {product.name} {colour.upper()} to your cart ')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {cart[item_id]} {product.name} in your cart ')

        else:
            cart[item_id] = quantity
            messages.success(request, f'You Added {product.name} to your cart ')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjusts the quantity from the cart template
    """
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    cart = request.session.get('cart', {})

    if colour:
        if quantity > 0:
            cart[item_id]['items_by_colour'][colour] = quantity
            messages.success(request, f'There are now {cart[item_id]["items_by_colour"][colour]} {product.name} with the colour {colour.upper()} in your cart')
        else:
            del cart[item_id]['items_by_colour'][colour]
            if not cart[item_id]['items_by_colour']:
                cart.pop(item_id)
                messages.success(request, f'You removed {product.name} with the colour {colour.upper()} to your cart ')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'There are now {cart[item_id]} {product.name} in your cart ')
        else:
            cart.pop(item_id)
            messages.success(request, f'You removed {product.name} from your cart ')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_cart(request, item_id):
    """
    Removes items from the cart
    """
    try:
        product = get_object_or_404(Products, pk=item_id)
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']
        cart = request.session.get('cart', {})

        if colour:
            if quantity > 0:
                del cart[item_id]['items_by_colour'][colour]
                if not cart[item_id]['items_by_colour']:
                    cart.pop(item_id)
                messages.success(request, f'You removed {cart[item_id]["items_by_colour"][colour]} {product.name} with the colour {colour.upper()} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'You removed {product.name} from your cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
  
    except Exception as e:
        messages.error(request, f'There was an error removing item: {e} from the cart')
        return HttpResponse(status=500)
