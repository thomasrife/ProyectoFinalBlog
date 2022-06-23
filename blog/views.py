from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class Home(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha')
    template_name ='home.html'
    paginate_by = 3

class BlogList(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha')
    template_name='blog/blog_list.html'
    paginate_by = 2
    
class BlogCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogDelete(DeleteView):
    model = Post
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
