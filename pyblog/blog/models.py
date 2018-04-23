from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")


    def __str__(self):
        return self.title

    
    def was_published_recently(self, ref_point=None):
        if not ref_point:
            ref_point = timezone.now()
        return ref_point - datetime.timedelta(days=1) <= self.pub_date <= ref_point


    # def get_absolute_url(self):
    #     if self.status == 'p'
    #         return "/article/%i/" % self.id
    #     else:
    #         return "/preview/article/%i/" % self.id

    # @models.permalink
    # def get_absolute_url(self):
    #     if self.status == 'p'
    #         return ('post.views.details', [str(self.id)])
    #     else:
    #         return ('post.views.preview', [str(self.id)])



class Comment(models.Model):
    article = models.ForeignKey(Article)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author_name



class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)     


def __str__(self):
        return self.author_name
    
    