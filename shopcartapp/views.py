from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from mainapp.models import Product
from mainapp.views import shopping_cart
from shopcartapp.models import ShoppingCart


@login_required
def cart(request):
    context = {
        'title': 'корзина',
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
@ensure_csrf_cookie
def cart_remove(request):
    if request.is_ajax() and request.method == 'POST':
        pk = int(request.POST['pk'])
        item = get_object_or_404(ShoppingCart, pk=pk)
        item.quantity = 0
        item.save()

        context = {
            'shopping_cart': shopping_cart(request.user).order_by('product__category'),
        }

        result = render_to_string('shopcartapp/inc_cart_list.html', context)

        return JsonResponse({'result': result})

@login_required
@ensure_csrf_cookie
def cart_edit(request):
    if request.is_ajax() and request.method == 'POST':
        pk = int(request.POST['pk'])
        quantity = int(request.POST['quantity'])
        cart_item = ShoppingCart.objects.get(pk=pk)
        err = {}
        
        if 0 < quantity <= cart_item.product.quantity or quantity == 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            err = {
                'item_pk': cart_item.pk,
                'msg': 'кол-во товара ограничего'
            }
        
        context = {
            'err_quantity': err,
            'shopping_cart': shopping_cart(request.user).order_by('product__category'),
        }

        result = render_to_string('shopcartapp/inc_cart_list.html', context)
        
        return JsonResponse({'result':result})
