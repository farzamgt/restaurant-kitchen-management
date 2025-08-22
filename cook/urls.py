from django.urls import path
from .views import (
    CookSignupView,
    CookLoginView,
    CookLogoutView,
    DashboardView
)


app_name = 'cook'
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", CookSignupView.as_view(), name="signup"),
    path("login/", CookLoginView.as_view(), name="login"),
    path("logout/", CookLogoutView.as_view(), name="logout"),
]
