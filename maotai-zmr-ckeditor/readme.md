- [1. 实现了ckeditor和prismjs样式](#1-实现了ckeditor和prismjs样式)
- [2. 展示效果](#2-展示效果)
- [3. 实现方式](#3-实现方式)
- [4. 设置app,实现后台ck,和前台展示](#4-设置app,实现后台ck,和前台展示)
- [5. 代码高亮支持](#5-代码高亮支持)
- [6. 拖拽图片到编辑器](#6-拖拽图片到编辑器)
- [7. 附-完整的ck插件配置](#7-附-完整的ck插件配置)


# 1. 实现了ckeditor和prismjs样式
https://github.com/galetahub/ckeditor/
http://prismjs.com/download.html

# 2. 展示效果
- 可以上传图片到服务器
![girl01.png](https://github.com/lannyma/maotai-zmr-ckeditor/raw/master/media/girl01.png)
- 可以本地复制图片粘贴(外链的方式)
![girl02.png](https://github.com/lannyma/maotai-zmr-ckeditor/raw/master/media/girl02.png)
- 支持代码行高亮/行号
![code.png](https://github.com/lannyma/maotai-zmr-ckeditor/raw/master/media/code.png)
- 后台文本编辑样式
![houtai.png](https://github.com/lannyma/maotai-zmr-ckeditor/raw/master/media/houtai.png)
# 3. 实现方式
参考: http://www.aaron-zhao.com/post/1/

1.安装相关包
```
pip install django-ckeditor
pip install pillow
```
2.设置setting.py

- 2.1图片将上传到项目下的media/upload
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'upload/'
```
- 2.2生成缩略图
CKEDITOR_IMAGE_BACKEND = 'pillow'

- 2.3设置编辑器的一些插件
```
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [  #这里是编辑器的各种功能按钮
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
```
说明: 其中toolbar_Custom里就是编辑器的各种功能按钮，我们可以根据个人喜好调整按钮的位置、顺序、组合，添加删除功能按钮，更多的功能请参考官方文档。

- 3.3如需禁止上传图片以外的其他文件，则需要设置
```
CKEDITOR_ALLOW_NONIMAGE_FILES = False
```

# 4. 设置app,实现后台ck,和前台展示

- 4.1新建app

- 4.2设置url
```
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    # url(r'', include('blog.urls')),
    url(r'', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #没有这一句无法显示上传的图片
```

- 4.3 设置 blog/models.py,并同步数据库,并createsuperuser
```
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True,verbose_name='正文')

    def __str__(self):
        return self.title
```
- 4.4 设置blog/views
```
from blog.models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})

```
- 4.5打开后台添加文章即可以看到编辑器
- 4.6打开前台可以看到文章

# 5. 代码高亮支持
- 下载http://download.ckeditor.com/prism/releases/prism_1.0.1.zip
- 解压到static/ckeditor/ckeditor/plugins(即python安装包的site-packege/xxx下)
- 前端需要引用的
```
'extraPlugins': ','.join(['codesnippet','widget','lineutils',]),
```
```
<script src="{% static 'ckeditor/ckeditor/plugins/prism/lib/prism/prism_patched.min.js' %}"></script>
```
- 顶部的css可以在这里下载
  - http://prismjs.com/download.html
  ```
  <link rel="stylesheet" href="{% static 'blog/css/prism.css' %}">
  ```
  - 

# 6. 拖拽图片到编辑器

在编辑器里之间copy/paste图片或者从桌面、文件夹直接拖拽图片到编辑器，需要用到插件uploadimage，在CKEDITOR_CONFIGS里设置：
```
'extraPlugins' : ['codesnippet', 'uploadimage',]
```

# 7. 附-完整的ck插件配置
```
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'language':'zh-cn',
        'width': '750px',
        'height': '500px',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
                       '-','JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['Image', '-', 'Flash', 'Iframe', '-', 'Table', 'CodeSnippet', 'Templates']},
            '/',
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'special', 'items': ['Subscript', 'Superscript', '-', 'HorizontalRule',
                                          'SpecialChar', 'Smiley']},
            {'name': 'tools', 'items': ['Undo', 'Redo', '-', 'Source', 'Preview', 'Save', '-', 'Maximize']}
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet',
                'uploadimage',
                'prism',
            ]),
    }
}
```

注:如果代码要显示行号需要勾选prism网站上的这个后再下载:
![hanghao.png](https://github.com/lannyma/maotai-zmr-ckeditor/raw/master/media/hanghao.png)
