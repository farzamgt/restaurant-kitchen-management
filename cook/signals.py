from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Cook
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out
)


@receiver(post_save, sender=Cook)
def welcome_new_cook(sender, instance, created, **kwargs):
    if created:
        print(f"Welcome {instance.username} to the restaurant system!")


@receiver(user_logged_in)
def cook_logged_in(sender, request, user, **kwargs):
    print(f"{user.username} logged in")


@receiver(user_logged_out)
def cook_logged_out(sender, request, user, **kwargs):
    print(f"{user.username} logged out")
