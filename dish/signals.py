from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Dish


@receiver(post_save, sender=Dish)
def dish_saved_message(sender, instance, created, **kwargs):
    if created:
        print(f"Dish '{instance.name}' was created successfully!")
    else:
        print(f"Dish '{instance.name}' was updated successfully!")
