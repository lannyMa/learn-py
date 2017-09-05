from django.shortcuts import render
from firstapp.models import Article
# Create your views here.

def index(request):

    queryset=request.GET.get("tag")
    if queryset:
        articles = Article.objects.filter(tag=queryset)
    else:
        articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})