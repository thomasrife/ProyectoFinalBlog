from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

#=========================== VISTAS GENERICAS DE BLOG ==============================
class Home(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha')
    template_name ='home.html'
    paginate_by = 2

class BlogList(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha')
    template_name='blog/blog_list.html'
    paginate_by = 2
    

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
    
        # def test_fun(self):
        #     exist = Post.objects.filter( autor=self.request.user.id, id=self.kwargs['pk'])
        #     return True if exist else False
 
 #======================== VISTAS GENERICA DE NOSOTROS ==========================
 