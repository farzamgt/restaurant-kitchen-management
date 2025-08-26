from django.urls import path

from .views import (
    ActivateCookView,
    CookListView,
    CookLoginView,
    CookLogoutView,
    CookSignupView,
    DashboardView,
    ProfileView,
    WelcomeView
)

app_name = 'cook'
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", CookSignupView.as_view(), name="signup"),
    path("welcome/", WelcomeView.as_view(), name="welcome"),
    path(
        "activate/<int:pk>/",
        ActivateCookView.as_view(),
        name="activate"
    ),
    path("login/", CookLoginView.as_view(), name="login"),
    path("logout/", CookLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("all/", CookListView.as_view(), name="cook_list"),
]
