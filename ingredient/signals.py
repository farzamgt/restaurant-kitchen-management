from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ingredient


@receiver(post_save, sender=Ingredient)
def ingredient_saved_log(sender, instance, created, **kwargs):
    if created:
        print(f"Ingredient '{instance.name}' was created.")
    else:
        print(f"Ingredient '{instance.name}' was updated.")
