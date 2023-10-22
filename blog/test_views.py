from django.test import TestCase


class TestViews(TestCase):
    """
     Unitests for testing app views
     """
    def test_home_page(self):
        """Tests if home page renders correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_page(self):
        """Tests if recipes page renders correctly"""
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_add_recipe_page(self):
        """Tests if add_recipe page renders correctly"""
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_category_page(self):
        """Tests if category page renders correctly"""
        response = self.client.get('/category/<category>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
