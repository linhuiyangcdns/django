# -*- coding:utf-8 -*-


from django.db import models
from django.urls import reverse


#作者
class Author(models.Model):
    name = models.CharField(max_length= 30)
    #email = models.CharField(blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# 分类
class Categroy(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='最后修改时间')
    excerpt = models.CharField(max_length=100,blank=True,verbose_name='摘要')
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True)
    category = models.ForeignKey(Categroy)
    view = models.IntegerField(default=0,verbose_name='阅读量')

    def increase_views(self):
        self.view += 1
        self.save(update_fields=['view'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']