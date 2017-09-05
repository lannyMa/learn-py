

![girl.png](https://github.com/lannyma/testgit/raw/master/media/girl.jpg)
## 这里主要体现了django的模版继承
![blog.png](https://github.com/lannyMa/maotai-blogproject/raw/master/media/blog.png)

## 实现了
- 文章的展示
- 后台添加文章
  - 标题
  - 内容
  - 时间戳
  - 根据时间戳排序
- 模版的继承
```
class BlogPost(models.Model):
    title = models.CharField(max_length=44)
    content = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering=['-timestamp']
```
## todo:
给管理页面增加搜索、自定义排序、过滤等功能。舍得不再就这些问题
