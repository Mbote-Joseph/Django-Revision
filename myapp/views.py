from pyexpat import model
from django.shortcuts import render
# from django.generics import ListView, DetailView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.
def index(request):
    name= "Joseph"
    form=PostForm
    return render(request, 'index.html', {'name': name, 'form': form})

class PostList(ListView):
    model = Post
    template_name = 'myapp/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

class CommentList(ListView):
    model = Comment
    template_name = 'myapp/comment.html'
    context_object_name = 'comments'
    paginate_by = 5
    ordering = ['-created_at'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'myapp/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentDetail(DetailView):
    model = Comment
    template_name = 'myapp/comment_detail.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context 




