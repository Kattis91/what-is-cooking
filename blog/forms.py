from .models import Recipe, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title', 'category', 'featured_image', 'ingredients',
            'instructions', 'estimated_time', 'servings',)
        widgets = {
            'instructions': SummernoteWidget(),
            'ingredients': forms.Textarea(
                attrs={'placeholder':
                       'Please write one ingredient per line'}),
            'estimated_time': forms.NumberInput(
                attrs={'placeholder': 'Estimated time is counted in minutes'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
