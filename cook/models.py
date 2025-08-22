from django.contrib.auth.models import AbstractUser
from django.db import models

class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
