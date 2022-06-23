from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegristoForm
from blogger.models import Avatar

class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'blogger/signUp.html'
    form_class = RegristoForm
    success_url = reverse_lazy('blog:home')
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"
    

class BloggerProfile(DetailView):

    model = User
    template_name = "blogger/blogger_detail.html"


class BloggerUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "blogger/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("blogger_profile", kwargs={"pk": self.request.user.id})

