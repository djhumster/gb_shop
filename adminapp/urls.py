from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from django.views.generic import TemplateView

import adminapp.views as adminapp

app_name='adminapp'

urlpatterns = [
    path('', user_passes_test(lambda u: u.is_staff)(TemplateView.as_view(
        template_name='adminapp/index.html')), name='index'),
    path('cat-list/', adminapp.CategoryListView.as_view(
        extra_context={'title': 'категории', 'mode': 'cat_list'}), name='cat-list'),
    path('cat-create/', adminapp.CategoryCreateView.as_view(
        extra_context={'title': 'категории/создание'}), name='cat-create'),
    path('cat-edit/<int:pk>/', adminapp.CategoryUpdateView.as_view(
        extra_context={'title': 'категории/редактирование'}), name='cat-edit'),
    path('cat-remove/<int:pk>/', adminapp.CategoryDeleteView.as_view(
        extra_context={'title': 'категории/удаление', 'mode': 'category'}), name='cat-remove'),
    path('user-list/', adminapp.UserListView.as_view(
        extra_context={'title': 'пользователи', 'mode': 'user_list'}), name='user-list'),
    path('user-create/', adminapp.UserCreateView.as_view(
        extra_context={'title': 'пользователи/создание'}), name='user-create'),
    path('user-edit/<int:pk>/', adminapp.UserUpdateView.as_view(
        extra_context={'title': 'пользователи/редактирование'}), name='user-edit'),
    path('user-remove/<int:pk>/', adminapp.UserDeleteView.as_view(
        extra_context={'title': 'пользователи/удаление', 'mode': 'user'}), name='user-remove'),
    path('product-list/', adminapp.ProductListView.as_view(
        extra_context={'title': 'продукты'}), name='product-list'),
]
