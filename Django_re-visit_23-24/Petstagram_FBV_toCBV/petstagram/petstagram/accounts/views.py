from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views

from petstagram.main_app.forms import ProfileCreateForm


# Create your views here.
class RegisterView(gen_views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'main/profile_create.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView(gen_views.DetailView):
    pass


class ProfileEditView(gen_views.UpdateView):
    pass


class ChangePasswordView(auth_views.PasswordChangeView):
    pass
