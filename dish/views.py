from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import DishType, Dish
from .forms import DishForm


class DishTypeListView(ListView):
    model = DishType
    template_name = "dish/dishtype_list.html"
    context_object_name = "dishtypes"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


class DishTypeCreateView(CreateView):
    model = DishType
    fields = ["name"]
    template_name = "dish/dishtype_form.html"
    success_url = reverse_lazy("dish:dishtype_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Dish type '{form.instance.name}' was created successfully!")
        return response


class DishTypeUpdateView(UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "dish/dishtype_form.html"
    success_url = reverse_lazy("dish:dishtype_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Dish type'{form.instance.name}' was updated successfully!")
        return response


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "dish/dishtype_confirm_delete.html"
    success_url = reverse_lazy("dish:dishtype_list")


class DishListView(ListView):
    model = Dish
    template_name = "dish/dish_list.html"
    context_object_name = "dishes"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(dish_type__name__icontains=query)
            ).distinct()
        return qs


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Dish '{form.instance.name}' was created successfully!")
        return response


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish/dish_detail.html"
    context_object_name = "dish"


class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"

    def get_success_url(self):
        return reverse_lazy("dish:dish_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Dish '{form.instance.name}' was updated successfully!")
        return response


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "dish/dish_confirm_delete.html"
    success_url = reverse_lazy("dish:dish_list")
