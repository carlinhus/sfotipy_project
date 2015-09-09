from django.db import models

from artists.models import Artist
class Album(models.Model):
    title=models.CharField(max_length=255)
    cover=models.ImageField(upload_to='albums')
    artist=models.ForeignKey(Artist)

    def __str__(self):
    	return self.title

    def showCover(self):
        return "<a href='%s' target='_blank'><img src='%s' width='50'></a>" % (self.cover.url, self.cover.url)
    showCover.allow_tags = True
