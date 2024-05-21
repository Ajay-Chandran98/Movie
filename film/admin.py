# film/admin.py
from django.contrib import admin
from .models import Command, Rating


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'movie__title')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'movie__title')


