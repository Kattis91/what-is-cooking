from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title', 'category', 'featured_image', 'author', 'ingredients',
            'instructions', 'estimated_time', 'servings',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
