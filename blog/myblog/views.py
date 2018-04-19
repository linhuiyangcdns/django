from django.shortcuts import render,get_object_or_404
from ..myblog.models import *
from ..comments.forms import CommentForms
import markdown


def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


# def detail(request,pk):
#     post = get_object_or_404(Post,pk = pk)
#     return render(request,'blog/detail.html',context={'post':post})


def archives(request,year, mouth):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__mouth=mouth
                                   ).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForms()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)
