
from ..models import Post,Category
from django import template


register = template.Library()


@register.simple_tag
def get_recent_posts(num= 5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'mouth', order='DESC')
    # order = 'DESC'表明降序排列


@register.simple_tag
def get_category():
    return Category.objects.all()