from __future__ import unicode_literals
import datetime
from django.db import models
from bookcase.models import BookCase
from authors.models import Author

YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]


class Books(models.Model):
    book_case = models.ForeignKey(BookCase)
    title = models.CharField(max_length=24)
    authors = models.ManyToManyField(Author)
    sub_topic = models.CharField(max_length=24)
    publisher = models.CharField(max_length=24)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=24)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.date.today().year)

    class Meta:
        verbose_name_plural = 'book'

    def __unicode__(self):
        return self.title
