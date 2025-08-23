from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import DishType, Dish
from .forms import DishForm

class DishTypeListView(ListView):
    model = DishType
    template_name = "dish/dishtype_list.html"

class DishTypeCreateView(CreateView):
    model = DishType
    fields = ["name"]
    template_name = "dish/dishtype_form.html"
    success_url = reverse_lazy("dish:dishtype_list")

class DishTypeUpdateView(UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "dish/dishtype_form.html"
    success_url = reverse_lazy("dish:dishtype_list")

class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "dish/dishtype_confirm_delete.html"
    success_url = reverse_lazy("dish:dishtype_list")


class DishListView(ListView):
    model = Dish
    template_name = "dish/dish_list.html"

class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish_list")

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish_list")

class DishDeleteView(DeleteView):
    model = Dish
    template_name = "dish/dish_confirm_delete.html"
    success_url = reverse_lazy("dish:dish_list")
