from django.urls import path

import adminapp.views as adminapp

app_name='adminapp'

urlpatterns = [
    path('cat-list/', adminapp.category_list, name='cat-list'),
    path('cat-edit/<int:pk>/', adminapp.category_edit, name='cat-edit'),
    path('cat-remove/<int:pk>/', adminapp.category_remove, name='cat-remove'),
    path('cat-create/', adminapp.category_create, name='cat-create'),
]