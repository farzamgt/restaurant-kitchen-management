from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredient:ingredient_list")


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredient/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredient:ingredient_list")
