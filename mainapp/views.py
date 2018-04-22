from django.shortcuts import render


links_menu = [
    {'href': 'index', 'name': 'главная'},
    {'href': 'category', 'name': 'телефоны'},
    {'href': 'category', 'name': 'ноутбуки'},
    {'href': 'category', 'name': 'телевизоры'},
    {'href': 'category', 'name': 'игровые приставки'},
    {'href': 'category', 'name': 'игры'},
    {'href': 'contacts', 'name': 'контакты'},
]

def index_view(request):
    return render(request, 'mainapp/index.html', {'links_menu': links_menu})
    
def category_view(request):
    return render(request, 'mainapp/category.html', {'links_menu': links_menu})

def contacts_view(request):
    return render(request, 'mainapp/contacts.html', {'links_menu': links_menu})
