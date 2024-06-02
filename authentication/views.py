# authentication/views.py

from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = CustomAuthenticationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('login')
