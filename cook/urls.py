from django.urls import path
from .views import (
    CookSignupView,
    CookLoginView,
    CookLogoutView,
    DashboardView,
    WelcomeView,
    activate_cook
)


app_name = 'cook'
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", CookSignupView.as_view(), name="signup"),
    path("welcome/", WelcomeView.as_view(), name="welcome"),
    path("activate/<int:pk>/", activate_cook, name="activate"),
    path("login/", CookLoginView.as_view(), name="login"),
    path("logout/", CookLogoutView.as_view(), name="logout"),
]
