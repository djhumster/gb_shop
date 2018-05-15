import random

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse

from mainapp.models import Category, Product
from shopcartapp.models import ShoppingCart


def shopping_cart(user=None):
    cart = []

    if user.is_authenticated:
        cart = ShoppingCart.objects.filter(user=user, quantity__gt=0)
    
    return cart

def get_same_products(pk=None, category=None):
    products = Product.objects.filter(category__pk=category).exclude(pk=pk)
    count = products.count()

    if count < 3:
        result = random.sample(list(products), count)
    else:
        result = random.sample(list(products), 3)
    
    return result

def index_view(request):
    context = {
        'title': 'главная',
        'shopping_cart': shopping_cart(request.user)
    }

    return render(request, 'mainapp/index.html', context)
    
def category_view(request, cat_url=None, page=1):
    category = get_object_or_404(Category, url_path=cat_url)
    products = Product.objects.filter(category=category, is_active=True, brand__is_active=True).order_by('name')
    paginator = Paginator(products, per_page=9)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': category.name,
        'products': products_paginator,
        'shopping_cart': shopping_cart(request.user)
    }
    
    return render(request, 'mainapp/category.html', context)

def contacts_view(request):
    context = {
        'title': 'контакты',
        'shopping_cart': shopping_cart(request.user)
    }

    return render(request, 'mainapp/contacts.html', context)

def product_view(request, cat_url=None, pk=None):
    product = get_object_or_404(Product, pk=pk)
    title = product.name

    context = {
        'title': title,
        'shopping_cart': shopping_cart(request.user),
        'product': product,
        'same_products': get_same_products(pk=product.pk, category=product.category.pk)
    }

    return render(request, 'mainapp/product.html', context)
