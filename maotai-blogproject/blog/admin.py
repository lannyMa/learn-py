# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import BlogPost
from django.contrib import admin

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)