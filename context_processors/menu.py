from django.template.context_processors import request

from mainapp.models import Category

def categories_menu(request):
    links = []
    categories = Category.objects.filter(is_active=True)

    for category in categories:
        links.append({
            'cat_url': category.url_path,
            'cat_name': category.name,
            'cat_id': category.pk,
        })
    
    return {'categories_links': links}
