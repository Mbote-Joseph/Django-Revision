from django.shortcuts import render
# from django.generics import ListView, DetailView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.
def index(request):
    name= "Joseph"
    posts=Post.objects.all()
    # p=Post.object.
    for post in posts:
        post.comment=post.post_comment.all()

    form = CommentForm
    total=posts.count()
    return render(request, 'index.html', {'name': name, 'form': form, 'posts': posts, 'total': total})
