import random

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse

from mainapp.models import Category, Product
from mainapp.forms import ContactForm
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

def get_paginator(query_set, page):
    paginator = Paginator(query_set, per_page=9)

    try:
        query_paginator = paginator.page(page)
    except PageNotAnInteger:
        query_paginator = paginator.page(1)
    except EmptyPage:
        query_paginator = paginator.page(paginator.num_pages)
    
    return query_paginator

def index_view(request):
    context = {
        'title': 'главная',
        'shopping_cart': shopping_cart(request.user)
    }

    return render(request, 'mainapp/index.html', context)
    
def category_view(request, cat_url=None, page=1):
    category = get_object_or_404(Category, url_path=cat_url)
    products = Product.objects.filter(category=category, is_active=True, brand__is_active=True).order_by('name')

    context = {
        'title': category.name,
        'products': get_paginator(products, page),
        'shopping_cart': shopping_cart(request.user)
    }
    
    return render(request, 'mainapp/category.html', context)

def contacts_view(request):
    context = {
        'title': 'контакты',
        'shopping_cart': shopping_cart(request.user)
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Тут должна быть отправка сообщения через send_mail из django.core.mail
            print(f'Отправитель: {sender}\nEmail: {email}\nТема: {subject}\nТекст:\n{message}')
        else:
            context['form'] = form
    else:
        context['form'] = ContactForm()

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

def search_view(request):
    if request.GET['q']:
        page = request.GET.get('page') or 1
        products = Product.objects.filter(name__icontains=request.GET['q'], is_active=True, brand__is_active=True).order_by('name')

        context = {
            'title': 'поиск',
            'products': get_paginator(products, page),
            'shopping_cart': shopping_cart(request.user),
            'question': request.GET['q']
        }

        return render(request, 'mainapp/search.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))
