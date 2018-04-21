# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField()


    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey(Article)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author_name


    
    