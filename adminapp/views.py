from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from adminapp.forms import CategoryForm, ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


class UserIsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class UserIsSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


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


class UserListView(UserIsSuperUserMixin, ListView):
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


class ProductListView(UserIsStaffMixin, ListView):
    model = Product
    template_name = 'adminapp/product_list.html'
    paginate_by = 20


class ProductCreateView(UserIsStaffMixin, CreateView):
    pass


class ProductUpdateView(UserIsStaffMixin, UpdateView):
    pass


class ProductDeleteView(UserIsSuperUserMixin, DeleteView):
    pass
