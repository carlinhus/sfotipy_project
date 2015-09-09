from django.db import models

from albums.models import Album
from artists.models import Artist

class Track(models.Model):
    title=models.CharField(max_length=255)
    order=models.PositiveIntegerField()
    track_file=models.FileField(upload_to='tracks')
    album=models.ForeignKey(Album)
    artist=models.ForeignKey(Artist)

    def __str__(self):
    	return self.title

    def play(self):
        return "<audio controls> <source src='%s' type='audio/mpeg'>Your browser doesn't support audio HTML5 tag</audio>" % self.track_file.url

    play.allow_tags = True 
