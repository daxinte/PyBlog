# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article
from django import forms
from .forms import CommentForm

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
            return redirect('detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_article.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('view.detail', pk=article.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('view.detail', pk=article.pk)
