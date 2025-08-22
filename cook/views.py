from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Cook
from .forms import CookSignupForm
from django.contrib.auth.views import LoginView, LogoutView


class CookSignupView(CreateView):
    model = Cook
    form_class = CookSignupForm
    template_name = "cook/signup.html"
    success_url = reverse_lazy("login")


class CookLoginView(LoginView):
    template_name = "cook/login.html"


class CookLogoutView(LogoutView):
    next_page = reverse_lazy("login")