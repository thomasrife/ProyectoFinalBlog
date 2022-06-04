from django.shortcuts import render
from blog.models import BlogModel
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"

class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"

class BlogCreate(CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogUpdate(UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

class BlogDelete(DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'
