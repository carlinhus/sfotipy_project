from django.db import models

class Artist(models.Model):
    fris_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255, blank=True)
    biography=models.TextField(blank=True)
