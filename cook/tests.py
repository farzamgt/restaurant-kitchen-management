from django.contrib.auth import get_user_model
from django.test import TestCase


Cook = get_user_model()


class CookModelTest(TestCase):
    def test_create_cook(self):
        cook = Cook.objects.create_user(
            username="testcook",
            password="password123",
            years_of_experience=5,
            is_active=True
        )
        self.assertEqual(cook.username, "testcook")
        self.assertEqual(cook.years_of_experience, 5)
        self.assertTrue(cook.is_active)

    def test_str_method(self):
        cook = Cook.objects.create_user(username="cookstr", password="12345")
        self.assertEqual(str(cook), "cookstr")
