# -*- coding:utf-8 -*-

from django.shortcuts import render,get_object_or_404
from .models import *
from comments.forms import CommentForms
import markdown
from django.views.generic import ListView,DetailView


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


#
# def index(request):
#     post_list = Article.objects.all().order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class PostDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView,self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForms()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


# def detail(request, pk):
#     post = get_object_or_404(Article, pk= pk)
#     post.increase_views()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       'markdown.extensions.toc',
#                                   ])
#     form = CommentForms()
#     comment_list = post.comment_set.all()
#     context = {'post': post,
#                'form': form,
#                'comment_list': comment_list
#                }
#     return render(request, 'blog/detail.html', context=context)


# 归档
def archives(request,year, month):
    post_list = Article.objects.filter(created_time__year =year,
                                       created_time__month = month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})


# 分类
# def category(request, pk):
#     post = get_object_or_404(Categroy, pk= pk)
#     post_list = Article.objects.filter(category= post).order_by('-created_time')
#     return render(request,'blog/index.html', context={'post_list':post_list})


class CategoryView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Categroy, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


def article(request):
    post_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/article.html', context={'post_list': post_list})


def resource(request):
    return render(request, 'blog/resource.html')


def timeLine(request):

    return render(request, 'blog/timeline.html')


def about(request):
    return render(request,'blog/about.html')