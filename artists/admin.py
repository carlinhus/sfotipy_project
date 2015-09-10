from .models import Artist
from django.contrib import admin
from sfotipy.actions import export_as_excel
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    ordering = ("first_name", "last_name")
    actions = [export_as_excel]
    prepopulated_fields = {"slug": ("first_name","last_name",)}
