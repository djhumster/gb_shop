from django.urls import re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^(?P<cat_url>[\w\d-]+)/$', mainapp.category_view, name='category'),
]