from django.urls import path
from .views import (
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView
)

app_name = "dish"

urlpatterns = [
    path("", DishListView.as_view(), name="dish_list"),
    path("add/", DishCreateView.as_view(), name="dish_create"),
    path("<int:pk>/edit/", DishUpdateView.as_view(), name="dish_update"),
    path("<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("types/", DishTypeListView.as_view(), name="dishtype_list"),
    path("types/add/", DishTypeCreateView.as_view(), name="dishtype_create"),
    path("types/<int:pk>/edit/", DishTypeUpdateView.as_view(), name="dishtype_update"),
    path("types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dishtype_delete"),
]
