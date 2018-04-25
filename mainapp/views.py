from django.shortcuts import render
from .models import Category, Product


def make_menu():
    links = []
    category = Category.objects.all()

    for cat in category:
        links.append({
            'href':'category',
            'cat_url':cat.url_path,
            'name':cat.name
        })

    links.append({
        'href':'contacts',
        'name':'контакты'
    })

    return links

links_menu = make_menu()

def index_view(request):
    title = 'главная'

    return render(request, 'mainapp/index.html', {'title': title, 'links_menu': links_menu})
    
def category_view(request, cat_url):

    for links in links_menu:
        if links.get('cat_url') and links['cat_url'] == cat_url:
            title = links['name']
            break

    return render(request, 'mainapp/category.html', {'title': title, 'links_menu': links_menu})

def contacts_view(request):
    title = 'контакты'
    return render(request, 'mainapp/contacts.html', {'title': title, 'links_menu': links_menu})
