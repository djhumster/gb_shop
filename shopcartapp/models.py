from django.db import models
from django.conf import settings
from mainapp.models import Product


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateField(verbose_name='время', auto_now_add=True)
