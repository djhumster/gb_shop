from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from shopcartapp.models import ShoppingCart
from mainapp.models import Product

def cart(request):
    pass

def cart_add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    old_cart_item = ShoppingCart.objects.filter(user=request.user, product=product)

    if old_cart_item:
        old_cart_item[0].quantity += 1
        old_cart_item[0].save()
    else:
        new_cart_item = ShoppingCart(user=request.user, product=product)
        new_cart_item.quantity += 1
        new_cart_item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_remove(request, pk=None):
    pass
