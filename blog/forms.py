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
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
