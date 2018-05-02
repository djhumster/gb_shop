from django.core.management.base import BaseCommand
from mainapp.models import Category, Brand, Product
from authapp.models import ShopUser

import json, os

def load_from_json():
    with open('demo_data.json', 'r', encoding='utf8') as data:
        return json.load(data)


class Command(BaseCommand):
    def handle(self, *args, **options): 
        data = load_from_json()
        
        Category.objects.all().delete()

        for category in data['categories']:
            new_cat = Category(**category)
            print(f'Добавлена категория {new_cat}')
            new_cat.save()

        Brand.objects.all().delete()

        for brand in data['brands']:
            new_brand = Brand(**brand)
            print(f'Добавлен бренд {new_brand}')
            new_brand.save()

        Product.objects.all().delete()

        for product in data['products']:
            _category = Category.objects.get(name=product['category'])
            product['category'] = _category
            
            _brand = Brand.objects.get(name=product['brand'])
            product['brand'] = _brand

            new_product = Product(**product)
            print(f'Добавлен продукт {new_product}')
            new_product.save()

        ShopUser.objects.all().delete()

        super_user = ShopUser.objects.create_superuser('django',
            'email@example.com', 'geekbrains', age=30)
        print(f'Пользователь {super_user} создан!\nПароль: geekbrains')
