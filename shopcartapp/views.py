from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

from shopcartapp.models import ShoppingCart
from mainapp.models import Product
from mainapp.views import make_menu, shopping_cart

@login_required
def cart(request):
    context = {
        'title': 'корзина',
        'links_menu': make_menu(),
        'shopping_cart': shopping_cart(request.user).order_by('product__category')
    }
    return render(request, 'shopcartapp/shoppingcart.html', context)

@login_required
def cart_add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product',
                    kwargs={'pk': pk, 'cat_url': product.category.url_path}))
    
    try:
        old_cart_item = ShoppingCart.objects.get(user=request.user, product=product)
        old_cart_item.quantity += 1
        old_cart_item.save()
    except ObjectDoesNotExist:
        new_cart_item = ShoppingCart(user=request.user, product=product)
        new_cart_item.quantity += 1
        new_cart_item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_remove(request, pk=None):
    item = get_object_or_404(ShoppingCart, pk=pk)
    item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_edit(request, pk=None, quantity=None):
    if request.is_ajax():
        cart_item = ShoppingCart.objects.get(pk=pk)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

        context = {
            'shopping_cart': shopping_cart(request.user).order_by('product__category'),
        }

        result = render_to_string('shopcartapp/inc_cart_list.html', context)

        return JsonResponse({'result': result})