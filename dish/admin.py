from django.contrib import admin

from .models import Dish, DishType


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    list_filter = ("dish_type", "cooks")
    search_fields = ("name", "description")
    filter_horizontal = ("dish_type", "cooks", "ingredients")
