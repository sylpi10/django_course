from django.shortcuts import render
from django.http import HttpResponse
from songs.models import Song

# Create your views here.
def hello(request):
    return HttpResponse('hello appone')


def songs_list(request):
    names = []
    for s in Song.objects.all():
        names.append(s.name)

    body = '<br/>'.join(names)
    return HttpResponse(body)

def song_add(request, song_name, duration):
    song = Song(name=song_name, duration=duration)
    song.save()
    return HttpResponse("Song was added wiht id {}".format(song.pk))