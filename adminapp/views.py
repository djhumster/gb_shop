from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import (HttpResponseRedirect, get_object_or_404, render,
                              reverse)

from adminapp.forms import CategoryForm, ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


@user_passes_test(lambda u: u.is_superuser)
def admin_index(request):
    
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda u: u.is_superuser)
def category_list(request):
    title = 'категории'
    categories = Category.objects.all().order_by('name')

    return render(request, 'adminapp/cat-list.html', {'categories': categories, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def category_edit(request, pk=None):
    title = 'категории/редактирование'
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin:cat-list'))

    form = CategoryForm(instance=category)

    return render(request, 'adminapp/cat-edit.html', {'form': form, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def category_remove(request, pk=None):
    title = 'категории/удаление'
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()

        return HttpResponseRedirect(reverse('admin:cat-list'))
    else:
        return render(request, 'adminapp/delete-confirm.html', {'category': category, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/создание'
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin:cat-list'))

    form = CategoryForm()

    return render(request, 'adminapp/cat-edit.html', {'form': form, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    title = 'пользователи'
    users = ShopUser.objects.all()

    return render(request, 'adminapp/user-list.html', {'users': users, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('admin:user-list'))

    form = ShopUserRegisterForm()

    return render(request, 'adminapp/user-edit.html', {'form': form, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, pk=None):
    title = 'пользователи/редактирование'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        form = ShopUserAdminEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin:user-list'))

    form = ShopUserAdminEditForm(instance=user)

    return render(request, 'adminapp/user-edit.html', {'title': title, 'form': form})

@user_passes_test(lambda u: u.is_superuser)
def user_remove(request, pk=None):
    title = 'пользователи/удаление'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.delete()

        return HttpResponseRedirect(reverse('admin:user-list'))

    return render(request, 'adminapp/delete-confirm.html', {'user': user, 'title': title})
    