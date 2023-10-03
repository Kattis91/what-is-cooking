from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1, related_name='category')
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='published_recipes')
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredient',
        through_fields=('recipe', 'ingredient')
        )
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    estimated_time = models.IntegerField('estimated_time')
    servings = models.IntegerField('servings', default=4)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} | {self.author}'

    def number_of_likes(self):
        return self.likes.count()


class RecipeIngredient(models.Model):
    UNITS = [
        ('gr', 'Grams'),
        ('kg', 'Kilogram'),
        ('L', 'Litres'),
        ('mL', 'Millilitres'),
        ('tsp', 'Teaspoon'),
        ('tbsp', 'Tablespoon'),
        ('cup', 'Cup'),
        ('pieces', 'Pieces'),
        ('slices', 'Slices')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.CharField(max_length=100, choices=UNITS, default='gr')

    def __str__(self):
        return f'{self.ingredient} for {self.recipe}'
    

class Comment(models.Model):

    post = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name}'

