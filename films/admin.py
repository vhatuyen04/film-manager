# your_app/admin.py
from django.contrib import admin
from .models import Film

class FilmAdmin (admin.ModelAdmin):
    list_display = ('title', 'thubnail', 'youtube_url', 'film_file')

admin.site.register(Film)