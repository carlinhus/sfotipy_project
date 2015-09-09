from .models import Artist
from django.contrib import admin

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	pass
