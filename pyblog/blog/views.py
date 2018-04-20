# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from .forms import CommentForm
from .models import Article

# Create your views here.

def detail(request, article_id):
    details = "blog/detail.html"
    context = {
        "article": get_object_or_404(Article, id=article_id)
    }
    return render(request, details, context)



class IndexView(ListView):
    model = Article

index = IndexView.as_view()


def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            messages.success(request, 'Your comment was saved')
            url = reverse('detail', kwargs={'article_id': pk})
            return HttpResponseRedirect(url)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_article.html', {'form': form})
