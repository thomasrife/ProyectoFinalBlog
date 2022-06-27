from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

#=========================== VISTAS GENERICAS DE BLOG ==============================
class Home(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha')
    template_name ='home.html'
    paginate_by = 3
    
class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/aboutUs.html')
class BlogDetail(DetailView):
    model =  Post
    template_name = 'blog/blog_detail.html'
    

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
