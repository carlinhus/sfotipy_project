from django.db import models
from sfotipy.mixins import SlugMixin
from artists.models import Artist

class Album(SlugMixin, models.Model):
    title=models.CharField(max_length=255)
    cover=models.ImageField(upload_to='albums')
    artist=models.ForeignKey(Artist)
    slug = models.CharField(max_length=255, blank=True)

    def __str__(self):
    	return self.title

    def showCover(self):
        return "<a href='%s' target='_blank'><img src='%s' width='50'></a>" % (self.cover.url, self.cover.url)
    showCover.allow_tags = True

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.title, Album)
        super(Album, self).save(*args, **kwargs)


