from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import DishType, Dish
from .forms import DishForm
from django.db.models import Q


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
        form.instance._request = self.request
        return super().form_valid(form)

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("dish:dish_list")

    def form_valid(self, form):
        form.instance._request = self.request
        return super().form_valid(form)

class DishDeleteView(DeleteView):
    model = Dish
    template_name = "dish/dish_confirm_delete.html"
    success_url = reverse_lazy("dish:dish_list")


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish/dish_detail.html"
    context_object_name = "dish"
