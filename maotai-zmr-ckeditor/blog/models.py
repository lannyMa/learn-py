from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True,verbose_name='正文')

    def __str__(self):
        return self.title