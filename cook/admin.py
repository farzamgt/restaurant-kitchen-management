from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    model = Cook
    list_display = (
        "username",
        "email",
        "years_of_experience",
        "is_active",
        "is_staff"
    )
    list_filter = (
        "is_active", "is_staff", "years_of_experience"
    )
    search_fields = ("username", "email")
    ordering = ("username",)
