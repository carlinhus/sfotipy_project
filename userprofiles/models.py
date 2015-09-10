# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="avatars", default = "defaultavatar.jpg")
    user = models.OneToOneField(User)

