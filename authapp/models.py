from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='фото', upload_to='user_avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
