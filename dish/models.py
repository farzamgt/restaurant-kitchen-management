from django.db import models
from cook.models import Cook

class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)
    ingredients = models.ManyToManyField("ingredient.Ingredient", blank=True)
    photo = models.ImageField(upload_to="dishes/", blank=True, null=True)

    def __str__(self):
        return self.name
