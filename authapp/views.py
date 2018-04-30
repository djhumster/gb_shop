from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'вход'
    login_form = ShopUserLoginForm(data=request.POST)
    
    if request.method == 'POST' and login_form.is_valid():
        usrn = request.POST['username']
        pswd = request.POST['password']

        user = auth.authenticate(username=usrn, password=pswd)

        if user and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form
    }

    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('index'))

def register(request):    
    return HttpResponseRedirect(reverse('index'))

def edit(request):
    return HttpResponseRedirect(reverse('index'))