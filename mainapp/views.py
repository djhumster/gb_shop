from django.http import Http404
from django.shortcuts import render
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

def shopping_cart_count(request):
    cart_count = 0

    if request.user.is_authenticated:
        cart = ShoppingCart.objects.filter(user=request.user)

        for item in cart:
            cart_count += item.quantity

    return cart_count

def index_view(request):
    context ={
        'title': 'главная',
        'links_menu': make_menu(),
        'shopping_cart_count': shopping_cart_count(request)
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
        'shopping_cart_count': shopping_cart_count(request)
    }
    
    return render(request, 'mainapp/category.html', context)

def contacts_view(request):
    context ={
        'title': 'контакты',
        'links_menu': make_menu(),
        'shopping_cart_count': shopping_cart_count(request)
    }

    return render(request, 'mainapp/contacts.html', context)
