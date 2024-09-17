from django.contrib import admin
from .models import Genre, Film

class FilmAdmin (admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'youtube_url', 'film_file')
    search_fields = ('title',)
    list_filter = ('genres',)
    filter_horizontal = ('genres',)

admin.site.register(Genre)
admin.site.register(Film, FilmAdmin)