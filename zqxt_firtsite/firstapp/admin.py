from django.contrib import admin
from firstapp.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag',)
admin.site.register(Article,ArticleAdmin)