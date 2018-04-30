from django.http import Http404
from django.shortcuts import render
from .models import Category, Product


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

def index_view(request):
    context ={
        'title': 'главная',
        'links_menu': make_menu()
    }

    return render(request, 'mainapp/index.html', context)
    
def category_view(request, cat_url=None):
    title = None
    links_menu = make_menu()

    for link in links_menu:
        if link.get('cat_url') and link['cat_url'] == cat_url:
            title = link['name']
            products = Product.objects.filter(category_id=link['cat_id'])
            break
    
    if title is None:
        raise Http404('Категория не существует!')

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products
    }

    return render(request, 'mainapp/category.html', context)

def contacts_view(request):
    context ={
        'title': 'контакты',
        'links_menu': make_menu()
    }

    return render(request, 'mainapp/contacts.html', context)
