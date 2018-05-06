from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse

from mainapp.views import make_menu

def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST or None)
    
    if request.method == 'POST' and login_form.is_valid():
        usrn = request.POST['username']
        pswd = request.POST['password']

        user = auth.authenticate(username=usrn, password=pswd)

        if user and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
        'links_menu': make_menu()
    }

    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('index'))

def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            
            return HttpResponseRedirect(reverse('auth:login'))
    else:        
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form,
        'links_menu': make_menu()
    }

    return render(request, 'authapp/register.html', context)

def edit(request):
    title = 'профиль'

    if request.method == 'POST':

        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm()

    context = {
        'title': title,
        'edit_form': edit_form,
        'links_menu': make_menu()
    }

    return render(request, 'authapp/edit.html', context)
