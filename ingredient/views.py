from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import IngredientForm
from .models import Ingredient


class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredient/ingredient_list.html"
    context_object_name = "ingredients"
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Ingredient '{self.object.name}' created successfully!"
        )
        return response


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Ingredient '{self.object.name}' updated successfully!"
        )
        return response


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredient/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredient:ingredient_list")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(
            request,
            f"Ingredient '{obj.name}' deleted successfully!"
        )
        return super().delete(request, *args, **kwargs)
