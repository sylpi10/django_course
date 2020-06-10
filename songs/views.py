from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from songs.models import Song
from songs.forms import TestForm
from django.urls import reverse
from django.contrib import messages

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

# def thanks(request):
#     return HttpResponse('thanks, mail send')

def get_form_data(request):

    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():
            subject = 'New Message from {}'.format(form.cleaned_data['name'].capitalize())
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            print('email', form.cleaned_data['email'])
            send_mail(subject, message, from_email, ['syl.pillet@hotmail.fr'])
#             return HttpResponseRedirect(reverse('thanks'))
            messages.success(request, 'Form submission successful')

    else:
        form = TestForm()
    return render(request, 'songs/form.html', {'form': form})
