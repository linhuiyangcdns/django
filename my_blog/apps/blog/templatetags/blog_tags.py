# -*- coding:utf-8 -*-

from ..models import Article,Categroy
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_article(num=4):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_hottest_article(num=8):
    return Article.objects.all().order_by('view')[:num]


@register.simple_tag
def get_categories():
    return Categroy.objects.all()


@register.simple_tag
def get_file():
    return Article.objects.dates('created_time','month', order='DESC')


@register.simple_tag
def get_days():
    return Article.objects.dates('created_time', 'day', order='DESC')


@register.simple_tag
def get_categories():
    return Categroy.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)