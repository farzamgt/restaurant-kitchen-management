from django import forms
from .models import Dish, DishType
from ingredient.models import Ingredient
from cook.models import Cook

class DishForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    dish_type = forms.ModelMultipleChoiceField(
        queryset=DishType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Dish
        fields = ["name", "price", "description", "dish_type", "cooks", "ingredients", "photo"]