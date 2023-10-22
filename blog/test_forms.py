from django.test import TestCase
from .forms import RecipeForm, CommentForm


class TestRecipeForm(TestCase):
    """
    Unittest for testing the add recipe form
    """
    def test_recipe_title_is_required(self):
        form = RecipeForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RecipeForm()
        self.assertEqual(
            form.Meta.fields, (
                'title', 'category', 'featured_image', 'ingredients',
                'instructions', 'estimated_time', 'servings')
        )


class TestCommentForm(TestCase):
    """
    Unittest for testing the comment form
    """
    def test_recipe_content_is_required(self):
        form = CommentForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('content',)
        )