from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from .models import Dish

@receiver(post_save, sender=Dish)
def dish_saved_message(sender, instance, created, **kwargs):
    if created:
        messages.success(instance._request, f"Dish '{instance.name}' was created successfully!")
    else:
        messages.success(instance._request, f"Dish '{instance.name}' was updated successfully!")
