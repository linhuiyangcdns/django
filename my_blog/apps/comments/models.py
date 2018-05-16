# -*- coding:utf-8 -*-

from django.db import models
from blog.models import Article


class Comment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length= 300,blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('blog.Article',on_delete=models.CASCADE)


    def __str__(self):
        return self.text[:20]