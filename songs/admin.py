from django.contrib import admin
from .models import Genre, Song
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SongAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'release_year', 'cost')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)