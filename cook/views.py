from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Cook
from .forms import CookSignupForm, CookProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "cook/dashboard.html"


class CookSignupView(CreateView):
    model = Cook
    form_class = CookSignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("cook:welcome")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created successfully! Please activate it.")
        return response


class CookLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm


class CookLogoutView(LogoutView):
    next_page = reverse_lazy("cook:login")


def activate_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    cook.is_active = True
    cook.save(update_fields=['is_active'])
    messages.success(request, "Your account has been activated! You can now log in.")
    return redirect('cook:login')


class WelcomeView(TemplateView):
    template_name = "accounts/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_cook = Cook.objects.latest('id')
        context['user'] = latest_cook
        return context


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Cook
    form_class = CookProfileForm
    template_name = "cook/profile.html"
    success_url = reverse_lazy("cook:cook_list")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "All changes saved successfully!")
        return response


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    template_name = "cook/cook_list.html"
    context_object_name = "cooks"
