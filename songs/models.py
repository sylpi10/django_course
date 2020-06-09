from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.artist_name)


class Song(models.Model):
    name = models.CharField(max_length=255, default='No name')
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    duration = models.IntegerField(default=0, help_text='duration in seconds')
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.name
