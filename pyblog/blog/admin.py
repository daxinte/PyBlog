# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3



class   ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]

    list_display = ('title', 'pub_date', 'was_published_recently')



admin.site.register(Article, ArticleAdmin)