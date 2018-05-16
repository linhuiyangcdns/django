from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForms


def get_comment(request, article_pk):
    post = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post)