# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
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
