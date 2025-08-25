from django.db import models
from cook.models import Cook
from cloudinary.models import CloudinaryField


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ManyToManyField(DishType)
    cooks = models.ManyToManyField(Cook)
    ingredients = models.ManyToManyField("ingredient.Ingredient", blank=True)
    photo = CloudinaryField("photo", blank=True, null=True)

    def __str__(self):
        return self.name
