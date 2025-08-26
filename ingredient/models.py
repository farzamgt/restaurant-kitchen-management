from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "ingredient"
        ordering = ["name"]
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name
