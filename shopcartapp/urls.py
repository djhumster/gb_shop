from django.urls import path
import shopcartapp.views as shopcartapp

app_name = 'shopcartapp'

urlpatterns = [
    path('', shopcartapp.cart, name='view'),
    path('add/<pk>/', shopcartapp.cart_add, name='add'),
    path('remove/<pk>/', shopcartapp.cart_remove, name="remove")
]
