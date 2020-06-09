from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hello(request):
    return HttpResponse('hello apptwo')


def pic_detail(request, category, year=0, month=0):
    template = loader.get_template('apptwo/index.html')

    context = {
         'pictures': [
            {
                'name': 'git',
                'filename': 'git-logo1.jpg',
            },
            {
                'name': 'springboot',
                'filename': 'springboot.png',
            },
            {
                'name': 'Angular',
                'filename': 'ang-01.png',
            },
         ]

    }
    return HttpResponse(template.render(context, request))
