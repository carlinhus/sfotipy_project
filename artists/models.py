from django.db import models
from sfotipy.mixins import SlugMixin

class Artist(SlugMixin, models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255, blank=True)
    biography=models.TextField(blank=True)
    slug = models.CharField(max_length=255, blank=True)

    def __str__(self):
    	return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.first_name + ' ' + self.last_name, Artist)
        super(Artist, self).save(*args, **kwargs)
