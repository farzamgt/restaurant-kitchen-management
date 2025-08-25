from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    avatar = CloudinaryField("avatar", blank=True, null=True)
