# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField()


class Comment(models.Model):
    article = models.ForeignKey(Article)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    