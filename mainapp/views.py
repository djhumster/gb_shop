from django.shortcuts import render


links_menu = [
    {'href': 'index', 'title': 'главная'},
    {'href': 'category', 'title': 'телефоны', 'cat_name': 'phones'},
    {'href': 'category', 'title': 'ноутбуки', 'cat_name': 'notebooks'},
    {'href': 'category', 'title': 'телевизоры', 'cat_name': 'tv'},
    {'href': 'category', 'title': 'игровые приставки', 'cat_name': 'consoles'},
    {'href': 'category', 'title': 'игры', 'cat_name': 'games'},
    {'href': 'contacts', 'title': 'контакты'},
]

def index_view(request):
    title = 'главная'
    return render(request, 'mainapp/index.html', {'title': title, 'links_menu': links_menu})
    
def category_view(request, cat_name):
    for links in links_menu:
        if links.get('cat_name') and links['cat_name'] == cat_name:
            title = links['title']

    return render(request, 'mainapp/category.html', {'title': title, 'links_menu': links_menu})

def contacts_view(request):
    title = 'контакты'
    return render(request, 'mainapp/contacts.html', {'title': title, 'links_menu': links_menu})
