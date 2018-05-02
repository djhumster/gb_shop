from django.core.management.base import BaseCommand
from mainapp.models import Category, Brand, Product
from authapp.models import ShopUser

import json, os

def load_from_json(file_name):
    pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('----------> YEAP <----------')
