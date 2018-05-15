from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView, MultipleObjectMixin

from adminapp.forms import (BrandForm, CategoryForm, ProductForm,
                            ShopUserAdminEditForm)
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Brand, Category, Product


class UserIsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class UserIsSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class PaginateByMixin(MultipleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = self.request.GET.get('paginate_by', '')

        return context

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by')

        if paginate_by:
            paginate_by = int(paginate_by)
        else:
            paginate_by = 25

        return paginate_by


class CategoryListView(UserIsStaffMixin, ListView):
    model = Category
    template_name = 'adminapp/list.html'


class CategoryCreateView(UserIsStaffMixin, CreateView):
    model = Category
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:cat-list')
    form_class = CategoryForm


class CategoryUpdateView(UserIsStaffMixin, UpdateView):
    model = Category
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:cat-list')
    form_class = CategoryForm


class CategoryDeleteView(UserIsSuperUserMixin, DeleteView):
    model = Category
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('admin:cat-list')


class UserListView(UserIsSuperUserMixin, PaginateByMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/list.html'


class UserCreateView(UserIsSuperUserMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:user-list')
    form_class = ShopUserRegisterForm


class UserUpdateView(UserIsSuperUserMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:user-list')
    form_class = ShopUserAdminEditForm


class UserDeleteView(UserIsSuperUserMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('admin:user-list')


class ProductListView(UserIsStaffMixin, PaginateByMixin, ListView):
    template_name = 'adminapp/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.request.GET.get('category', '')
        context['sort_by'] = self.request.GET.get('sort_by', '')

        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')

        if category:
            queryset = Product.objects.filter(category__pk=int(category))
        else:
            queryset = Product.objects.all()

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class ProductCreateView(UserIsStaffMixin, CreateView):
    model = Product
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:product-list')
    form_class = ProductForm


class ProductUpdateView(UserIsStaffMixin, UpdateView):
    model = Product
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:product-list')
    form_class = ProductForm


class ProductDeleteView(UserIsSuperUserMixin, DeleteView):
    model = Product
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('admin:product-list')


class BrandListView(ListView):
    model = Brand
    template_name = 'adminapp/list.html'


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:brand-list')
    form_class = BrandForm


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('admin:brand-list')
    form_class = BrandForm


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('admin:brand-list')
