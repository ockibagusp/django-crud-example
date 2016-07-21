from django.conf.urls import url
from authors import views

"""
urls_conf namespace = author

Perhatikan ini:
1. karena sifatnya hierarki dari url utama, coba lihat /crud/urls.py
prefix semua url diawali dengan /authors.

2. di template panggil alias lengkap dengan namespace nya.

contoh:
author:list
author:delete
"""
app_name = 'author'

urlpatterns = [
    url(r'^$', views.authorall, name="list"), # list merupakan alias dari url ini
    url(r'^new$', views.authornew, name="new"),
    url(r'^(?P<pk>\d+)$', views.authordetail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', views.authoredit, name="edit"),
    url(r'^delete/(?P<pk>\d+)$', views.authordelete, name="delete"),
]