from . import views
from django.urls import path

urlpatterns = [
    path("recipes/", views.RecipeList.as_view(), name="recipes"),
    path("", views.CategoryList.as_view(), name="categories"),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('update/<slug:slug>', views.UpdateRecipeView.as_view(), name='update')
]