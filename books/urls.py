from django.conf.urls import url
from books import views

"""
urls_conf namespace = book

Perhatikan ini:
1. karena sifatnya hierarki dari url utama, coba lihat /crud/urls.py
prefix semua url diawali dengan /books.

2. di template panggil alias lengkap dengan namespace nya.

contoh:
book:list
book:delete
"""
app_name = 'book'

urlpatterns = [
    url(r'^$', views.bookall, name="list"), # list merupakan alias dari url ini
    url(r'^new$', views.booknew, name="new"),
    url(r'^(?P<pk>\d+)$', views.bookdetail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', views.bookedit, name="edit"),
    url(r'^delete/(?P<pk>\d+)$', views.bookdelete, name="delete"),
]