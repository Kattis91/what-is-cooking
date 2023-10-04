from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title', 'category', 'featured_image', 'featured_image',
            'ingredients', 'instructions', 'estimated_time', 'servings',)