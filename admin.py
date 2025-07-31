from django.contrib import admin
from .models import Movie, MovieLink

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre', 'created_at')
    search_fields = ('title', 'description', 'genre')
    list_filter = ('genre', 'release_year', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MovieLink)
class MovieLinkAdmin(admin.ModelAdmin):
    list_display = ('movie', 'title', 'quality', 'is_working', 'created_at')
    search_fields = ('movie__title', 'title', 'url')
    list_filter = ('quality', 'is_working', 'created_at')
