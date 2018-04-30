from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64, unique=True)
    url_path = models.CharField(verbose_name='Имя категории в ссылке (eng)', max_length=48)
    desc = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(verbose_name='название', max_length=64)
    logo = models.ImageField(verbose_name='логотип', upload_to='brand_logos', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Название', max_length=64)
    short_desc = models.CharField(verbose_name='Короткое описание', max_length=255)
    full_desc = models.TextField(verbose_name='Полное описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='products', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'({self.category.name}) {self.brand} {self.name}'
