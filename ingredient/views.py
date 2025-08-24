from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Ingredient
from .forms import IngredientForm


class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredient/ingredient_list.html"
    context_object_name = "ingredients"


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Ingredient '{self.object.name}' created successfully!")
        return response


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Ingredient '{self.object.name}' updated successfully!")
        return response


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredient/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"Ingredient '{obj.name}' deleted successfully!")
        return super().delete(request, *args, **kwargs)
