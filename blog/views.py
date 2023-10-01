from django.shortcuts import render
from django.views import generic
from .models import Recipe, Category


def check_the_base(request):
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "recipes.html"
    pagination = 8


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"

