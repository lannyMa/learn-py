# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import BlogPost
# Create your views here.


def Article(request):
    articles = BlogPost.objects.all()
    return render(request,'archive.html',{ 'articles': articles})