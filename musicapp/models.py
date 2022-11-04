from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length= 400)
    last_name = models.CharField(max_length= 400)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length= 400)
    date_released = models.DateTimeField(default=datetime.today)
    likes = models.IntegerField()
    Artiste_id = models.CharField(max_length= 400) 

    def __str__(self):
        return self.name

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length= 500)
    song_id = models.CharField(max_length= 500)
    def __str__(self):
        return self.name