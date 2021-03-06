from django.urls import path
import shopcartapp.views as shopcartapp

app_name = 'shopcartapp'

urlpatterns = [
    path('', shopcartapp.cart, name='view'),
    path('add/<int:pk>/', shopcartapp.cart_add, name='add'),
    path('remove/', shopcartapp.cart_remove, name="remove"),
    path('edit/', shopcartapp.cart_edit)
]
