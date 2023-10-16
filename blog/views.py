from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Category
from .forms import RecipeForm, CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect


class CategoryList(generic.ListView):
    """
    Renders all objects of Category model
    """
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"


class CategoryListView(generic.ListView):
    """
    Allows to filter recipes by categories
    """
    template_name = "category.html"
    context_object_name = "catlist"

    # Source: https://www.youtube.com/watch?v=S9-Bt1JgRjQ&t=2137s
    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Recipe.objects.filter(
                category__name=self.kwargs['category'])
        }
        return content


class RecipeList(generic.ListView):
    """
    Renders all objects of Recipe model as a list
    """
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "recipes.html"
    paginate_by = 8


class RecipeDetail(View):
    """
    Displays recipe details in the view.
    Allows logged-in users to leave comments
    """
    def get(self, request, slug, *args, **kvargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        ingredients = recipe.ingredients.splitlines()
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'ingredients': recipe.ingredients.splitlines(),
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, slug, *args, **kvargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': comment_form
            }
        )


class AddRecipe(CreateView):
    """
    Allows logged-in users to publish recipes
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('recipes')

    # Source: https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post # noqa
    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class UpdateRecipeView(UpdateView):
    """
    Allows recipe authors (when logged in)
    to update their published recipes
    """
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
    """
    Allows recipe authors (when logged in)
    to delete their published recipes
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    # Source: https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item # noqa
    success_message = "Your recipe has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteRecipeView, self).delete(request, *args, **kwargs)


class RecipeLike(View):
    """
    Allows logged-in users to like/unlike recipes
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

