from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Recipe, Category, Ingredient, RecipeIngredient
from .forms import RecipeForm, IngredientForm
from django.forms import formset_factory
from django.template.defaultfilters import slugify


def check_the_base(request):
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "recipes.html"
    paginate_by = 8


class RecipeDetail(View):
    def get(self, request, slug, *args, **kvargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'ingredients': ingredients,
                'comments': comments,
                'liked': liked,
            }
        )


class AddRecipe(CreateView):
    """
    A class view for adding a recipe
    """

    def get(self, request, *args, **kwargs):
        recipe_form = RecipeForm()
        Ingredient_formset = formset_factory(
            IngredientForm, extra=10)

        context = {
            'recipe_form': recipe_form,
            'ingredient_form': IngredientForm(),
        }
        return render(request, 'add_recipe.html', context)
    
    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST)
        Ingredient_formset = formset_factory(
            IngredientForm, extra=10)
        
        ingredient_formset = Ingredient_formset(request.POST)

        recipe_form.instance.slug = slugify(request.POST['title'])

        if recipe_form.is_valid():
            recipe_form.save(commit=True)
            if ingredient_formset.is_valid():
                for ingredient_form in ingredient_formset:
                    ingredient.save(commit=True)
            return render(
                request,
                'add_recipe.html',
                {
                    'recipe_form': recipe_form,
                    'ingredient_form': IngredientForm(),
                }
            )


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"



              
