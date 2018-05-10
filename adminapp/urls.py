from django.urls import path

import adminapp.views as adminapp

app_name='adminapp'

urlpatterns = [
    path('', adminapp.admin_index, name='index'),
    path('cat-list/', adminapp.category_list, name='cat-list'),
    path('cat-edit/<int:pk>/', adminapp.category_edit, name='cat-edit'),
    path('cat-remove/<int:pk>/', adminapp.category_remove, name='cat-remove'),
    path('cat-create/', adminapp.category_create, name='cat-create'),
    path('user-list/', adminapp.user_list, name='user-list'),
    path('user-edit/<int:pk>/', adminapp.user_edit, name='user-edit'),
    path('user-remove/<int:pk>/', adminapp.user_remove, name='user-remove'),
    path('user-create/', adminapp.user_create, name='user-create'),
]