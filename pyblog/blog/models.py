from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title

    
    def was_published_recently(self, ref_point=None):
        if not ref_point:
            ref_point = timezone.now()
        return ref_point - datetime.timedelta(days=1) <= self.pub_date <= ref_point



class Comment(models.Model):
    article = models.ForeignKey(Article)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author_name


    
    