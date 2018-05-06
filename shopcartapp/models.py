from django.db import models
from django.conf import settings
from mainapp.models import Product


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateField(verbose_name='время', auto_now_add=True)

    def products_quantity(self):
        items = ShoppingCart.objects.filter(user=self.user)
        total_quantity = sum(list(map(lambda x: x.quantity, items)))

        return total_quantity

    def total_product_sum(self):
        return self.product.price * self.quantity

    def total_cart_sum(self):
        total_sum = 0
        items = ShoppingCart.objects.filter(user=self.user)
        
        for item in items:
            total_sum += item.product.price * item.quantity
        
        return total_sum
