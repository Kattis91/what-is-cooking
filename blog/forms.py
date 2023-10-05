from .models import Recipe, RecipeIngredient
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title', 'category', 'featured_image', 'author',
            'instructions', 'estimated_time', 'servings',)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'amount', 'unit',)