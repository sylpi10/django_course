from django.shortcuts import render
from django.http import HttpResponse
from devices.models import Device


def device_add(request, os, model):
    device = Device(os=os, model=model)
    device.save()
    return HttpResponse("created device {}".format(device))

def device_detail(request, id):
    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return HttpResponse(status=404)
    return HttpResponse(device)

def device_filter(request, os):
    device_names = []
    for d in Device.objects.filter(os=os):
        device_names.append(d.__str__())

    body = '<br>'.join(device_names)
    return HttpResponse(body)

def all(request):
   device_names = []
   devices = Device.objects.all()
   for d in devices:
       device_names.append(d.__str__())
   body = '<br>'.join(device_names)
   return HttpResponse(body)