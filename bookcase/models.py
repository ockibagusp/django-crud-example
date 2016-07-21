from __future__ import unicode_literals
import datetime
from django.db import models

BOOK_CASE_CHOICES = (
    (1, 'Computer Science'),
    (2, 'Religion'),
    (3, 'Philosophy'),
    (4, 'Laws'),
)


class BookCase(models.Model):
    book_case = models.IntegerField(choices=BOOK_CASE_CHOICES)

    def __unicode__(self):
        return self.get_book_case_display()
