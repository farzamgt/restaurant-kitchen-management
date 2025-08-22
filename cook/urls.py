from django.urls import path
from .views import CookSignupView, CookLoginView, CookLogoutView

urlpatterns = [
    path("signup/", CookSignupView.as_view(), name="signup"),
    path("login/", CookLoginView.as_view(), name="login"),
    path("logout/", CookLogoutView.as_view(), name="logout"),
]
