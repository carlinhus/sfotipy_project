from .models import Track
from django.contrib import admin

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "album", "artist", "slug", "play")
    ordering = ("album", "order")
    prepopulated_fields = {"slug": ("title",)}