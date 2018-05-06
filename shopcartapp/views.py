from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from shopcartapp.models import ShoppingCart
from mainapp.models import Product
from mainapp.views import make_menu, shopping_cart

@login_required
def cart(request):
    context = {
        'title': 'корзина',
        'links_menu': make_menu(),
        'shopping_cart': shopping_cart(request.user)
    }
    return render(request, 'shopcartapp/shoppingcart.html', context)

@login_required
def cart_add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    old_cart_item = ShoppingCart.objects.get(user=request.user, product=product)

    if old_cart_item:
        old_cart_item.quantity += 1
        old_cart_item.save()
    else:
        new_cart_item = ShoppingCart(user=request.user, product=product)
        new_cart_item.quantity += 1
        new_cart_item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_remove(request, pk=None):
    item = get_object_or_404(ShoppingCart, pk=pk)
    item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
