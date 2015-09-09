from .models import Track
from django.contrib import admin

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
	pass