# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<article_pk>[0-9]+)/$', views.get_comment, name='get_comment'),
]