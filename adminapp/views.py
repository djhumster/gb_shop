from django.shortcuts import (HttpResponseRedirect, get_object_or_404, render,
                              reverse)

from adminapp.forms import CategoryForm
from mainapp.models import Category, Product

# TODO: проверка прав доступа
def category_list(request):
    title = 'категории'
    categories = Category.objects.all().order_by('name')

    return render(request, 'adminapp/cat-list.html', {'categories': categories, 'title': title})

def category_edit(request, pk=None):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin:cat-list'))

    form = CategoryForm(instance=category)

    return render(request, 'adminapp/cat-edit.html', {'form': form})

def category_remove(request, pk=None):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()

        return HttpResponseRedirect(reverse('admin:cat-list'))
    else:
        return render(request, 'adminapp/delete_confirm.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin:cat-list'))

    form = CategoryForm()

    return render(request, 'adminapp/cat-edit.html', {'form': form})
