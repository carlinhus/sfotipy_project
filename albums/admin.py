"""
@author Carlos Campo

Copyleft license

"""
from .models import Album
from django.contrib import admin

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "showCover", "artist",)
    prepopulated_fields = {"slug": ("title",)}