from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'mainapp/index.html')
    
def category_view(request):
    return render(request, 'mainapp/category.html')

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')
