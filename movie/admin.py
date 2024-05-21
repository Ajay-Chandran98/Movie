# movie/admin.py
from django.contrib import admin
from .models import Movies, Category

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
