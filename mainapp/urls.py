from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<cat_url>/', mainapp.category_view, name='category'),
]