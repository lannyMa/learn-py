
# myfirstsite

## 实现了通过点标签过滤的功能:
通过点不同的tag,从后端数据库中查询出属于该tag的文章.
![tagfilter.png](https://github.com/lannyma/maotai-django/raw/master/zqxt_firtsite/meida/tagfilter.png)


views.py
```python
def index(request):

    queryset=request.GET.get("tag")
    if queryset:
        articles = Article.objects.filter(tag=queryset)
    else:
        articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})
```