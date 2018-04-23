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

    list_display = ('title', 'pub_date', 'was_published_recently', 'status', 'author')
    actions = ['make_published']


    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


    def make_published(self, request, queryset):
            rows_updated = queryset.update(status='p')
            if rows_updated == 1:
                message_bit = "1 story was"
            else:
                message_bit = "%s stories were" % rows_updated
            self.message_user(request, "%s successfully marked as published." % message_bit)


admin.site.register(Article, ArticleAdmin)