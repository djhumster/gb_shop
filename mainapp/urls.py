from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<cat_url>/', mainapp.category_view, name='category'),
    path('<cat_url>/page/<int:page>/', mainapp.category_view, name='page'),
    path('<cat_url>/<int:pk>/', mainapp.product_view, name='product')
]
