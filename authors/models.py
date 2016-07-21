from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'author'

    def __unicode__(self):
        return self.name
