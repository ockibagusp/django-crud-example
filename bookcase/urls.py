from django.conf.urls import url
from bookcase import views

"""
urls_conf namespace = bookcase

Perhatikan ini:
1. karena sifatnya hierarki dari url utama, coba lihat /crud/urls.py
prefix semua url diawali dengan /bookcase.

2. di template panggil alias lengkap dengan namespace nya.

contoh:
bookcase:list
bookcase:delete
"""
app_name = 'bookcase'

urlpatterns = [
    url(r'^$', views.bookcaseall, name="list"), # list merupakan alias dari url ini
    url(r'^new$', views.bookcasenew, name="new"),
    url(r'^(?P<pk>\d+)$', views.bookcasesdetail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', views.bookcaseedit, name="edit"),
    url(r'^delete/(?P<pk>\d+)$', views.bookcasedelete, name="delete"),
]