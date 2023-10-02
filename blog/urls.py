from . import views
from django.urls import path

urlpatterns = [
    path("recipes/", views.RecipeList.as_view(), name="recipes"),
    path("", views.CategoryList.as_view(), name="categories"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]