from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe, Category


def check_the_base(request):
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "recipes.html"
    pagination = 8


class RecipeDetail(View):
    def get(self, request, slug, *args, **kvargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'liked': liked,
            }
        )


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"

