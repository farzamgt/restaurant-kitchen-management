from django.test import TestCase

from cook.models import Cook
from ingredient.models import Ingredient

from .models import Dish, DishType


class DishModelTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="testcook",
            password="12345"
        )
        self.dish_type = DishType.objects.create(name="Starter")
        self.ingredient = Ingredient.objects.create(name="Tomato")
        self.dish = Dish.objects.create(
            name="Tomato Salad",
            description="Fresh tomato salad",
            price=5.99,
        )
        self.dish.cooks.add(self.cook)
        self.dish.dish_type.add(self.dish_type)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_creation(self):
        self.assertEqual(self.dish.name, "Tomato Salad")
        self.assertEqual(self.dish.price, 5.99)
        self.assertIn(self.cook, self.dish.cooks.all())
        self.assertIn(self.dish_type, self.dish.dish_type.all())
        self.assertIn(self.ingredient, self.dish.ingredients.all())
