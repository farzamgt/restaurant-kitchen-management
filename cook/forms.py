from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cook


class CookSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Cook
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "years_of_experience",
            "password1",
            "password2"
        ]
