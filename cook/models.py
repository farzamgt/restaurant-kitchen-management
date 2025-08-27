from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    avatar = CloudinaryField("avatar", blank=True, null=True)

    class Meta:
        db_table = "cook"
        ordering = ["username"]
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return self.username
