# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views
from .views import *

app_name = 'blog'
urlpatterns = [
    url(r'^index/$',views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(), name= 'detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^article/$', views.article, name='article'),
    url(r'^resource/$',views.resource,name='resource'),
    url(r'^timeline/$',views.timeLine,name='timeLine'),
    url(r'^about/$',views.about, name='about'),

]
handler404 = page_not_found
handler403 = permission_denied
handler500 = page_error