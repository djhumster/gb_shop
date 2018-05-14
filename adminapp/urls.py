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
    path('product-create/', adminapp.ProductCreateView.as_view(
        extra_context={'title': 'продукты/создание'}), name='product-create'),
    path('product-edit/<int:pk>/', adminapp.ProductUpdateView.as_view(
        extra_context={'title': 'продукты/редактирование', 'mode': 'product'}), name='product-edit'),
    path('product-remove/<int:pk>', adminapp.ProductDeleteView.as_view(
        extra_context={'title': 'пользователи/удаление'}), name='product-remove'),
    path('brand-list/', adminapp.BrandListView.as_view(
        extra_context={'title': 'бренды', 'mode': 'brand_list'}), name='brand-list'),
    path('brand-create/', adminapp.BrandCreateView.as_view(
        extra_context={'title': 'бренды/создание'}), name='brand-create'),
    path('brand-edit/<int:pk>/', adminapp.BrandUpdateView.as_view(
        extra_context={'title': 'бренды/редактирование'}), name='brand-edit'),
    path('brand-remove/<int:pk>/', adminapp.BrandDeleteView.as_view(
        extra_context={'title': 'бренды/удаление'}), name='brand-remove'),
]
