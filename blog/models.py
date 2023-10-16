from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


class Category(models.Model):
    """
    A model representing category.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def validate_nonzero(value):
    """
    Function to validate servings and estimated_time field values.
    """
    if value == 0:
        raise ValidationError(
            ('Please enter a value that is greater than zero'),
            params={'value': value},
        )


class Recipe(models.Model):
    """
    A recipe model to publish new recipes
    """
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='category')
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='published_recipes')
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    estimated_time = models.PositiveIntegerField(
        'estimated_time', validators=[
            validate_nonzero, MaxValueValidator(600)])
    servings = models.PositiveIntegerField(
        'servings', validators=[validate_nonzero, MaxValueValidator(50)])
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} | {self.author}'

    def number_of_likes(self):
        return self.likes.count()

    # Source: https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django # noqa
    def save(self, *args, **kwargs):
        """
        A method to generate slug for recipes
        submitted through the site form
        """
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    A comment model
    Before the comment is published, it needs to be approved by the admin
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name}'
