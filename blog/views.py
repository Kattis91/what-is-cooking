from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Category
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "recipes.html"
    paginate_by = 8


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


class AddRecipe(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been updated successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class DeleteRecipeView(SuccessMessageMixin, DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    success_message = "Your recipe has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteRecipeView, self).delete(request, *args, **kwargs)


class CategoryListView(generic.ListView):
    template_name = "category.html"
    context_object_name = "catlist"

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Recipe.objects.filter(
                category__name=self.kwargs['category'])
        }
        return content