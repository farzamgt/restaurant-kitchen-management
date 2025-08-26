from cloudinary.models import CloudinaryField
from django.db import models

from cook.models import Cook
from ingredient.models import Ingredient


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "dish_type"
        ordering = ["name"]
        verbose_name = "Dish Type"
        verbose_name_plural = "Dish Types"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ManyToManyField(DishType)
    cooks = models.ManyToManyField(Cook)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    photo = CloudinaryField("photo", blank=True, null=True)

    class Meta:
        db_table = "dish"
        ordering = ["name"]
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
