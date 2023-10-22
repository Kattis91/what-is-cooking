from django.test import TestCase
from .models import Recipe, Category, User, Comment


class RecipeModelTest(TestCase):
    # Source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#how_to_run_the_tests # noqa
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Fish')
        author = User.objects.create(username="admin")
        Recipe.objects.create(
            category=category, author=author, title='Test',
            ingredients='fish', instructions='cook', estimated_time='15',
            servings='3')

    def test_recipe_title_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)
