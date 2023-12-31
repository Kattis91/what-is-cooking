from django.contrib import admin
from .models import Recipe, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'category', 'created_on', 'slug')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    summernote_fields = ('ingredients', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'recipe', 'content', 'created_on', 'approved')
    search_fields = ('name', 'email', 'content')
    list_filter = ('created_on', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Category)
