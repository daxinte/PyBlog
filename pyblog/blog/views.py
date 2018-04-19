# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Article

# Create your views here.

def detail(request, article_id):
    pass
    

class IndexView(ListView):
    model = Article

index = IndexView.as_view()
