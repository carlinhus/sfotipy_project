# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile
from django.contrib import admin

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar")
    ordering = ("user",)