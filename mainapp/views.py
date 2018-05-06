from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Category, Product
from shopcartapp.models import ShoppingCart


def make_menu():
    links = []
    category = Category.objects.all()

    for cat in category:
        links.append({
            'href': 'products:category',
            'cat_url': cat.url_path,
            'name': cat.name,
            'cat_id': cat.id
        })

    links.append({
        'href':'contacts',
        'name':'контакты'
    })

    return links

def shopping_cart(user=None):
    cart = []

    if user.is_authenticated:
        cart = ShoppingCart.objects.filter(user=user)
    
    return cart

def index_view(request):
    context = {
        'title': 'главная',
        'links_menu': make_menu(),
        'shopping_cart': shopping_cart(request.user)
    }

    return render(request, 'mainapp/index.html', context)
    
def category_view(request, cat_url=None):
    title = None
    links_menu = make_menu()

    for link in links_menu:
        if link.get('cat_url') == cat_url:
            title = link['name']
            products = Product.objects.filter(category__pk=link['cat_id']).order_by('name')
            break
    
    if title is None:
        raise Http404('Категория не существует!')

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'shopping_cart': shopping_cart(request.user)
    }
    
    return render(request, 'mainapp/category.html', context)

def contacts_view(request):
    context = {
        'title': 'контакты',
        'links_menu': make_menu(),
        'shopping_cart': shopping_cart(request.user)
    }

    return render(request, 'mainapp/contacts.html', context)

def product_view(request, cat_url=None, pk=None):
    if not pk:
        return HttpResponseRedirect(reverse('index'))
    
    product = get_object_or_404(Product, pk=pk)
    title = product.name

    context = {
        'title': title,
        'links_menu': make_menu(),
        'shopping_cart': shopping_cart(request.user),
        'product': product
    }

    return render(request, 'mainapp/product.html', context)
