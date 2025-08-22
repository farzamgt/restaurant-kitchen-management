from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Cook
from .forms import CookSignupForm
from django.contrib.auth.views import LoginView, LogoutView


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "cook/dashboard.html"

class CookSignupView(CreateView):
    model = Cook
    form_class = CookSignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("cook:login")


class CookLoginView(LoginView):
    template_name = "accounts/login.html"


class CookLogoutView(LogoutView):
    next_page = reverse_lazy("cook:login")