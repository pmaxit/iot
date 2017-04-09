from django.shortcuts import render
from .forms import DeviceForm, CreateDeviceForm
from django.http import HttpResponse
from django_iot.apps.interactions.tasks import *

def index(request):
    if request.method == "POST":
        print request
        refresh_all.delay()
        return HttpResponse("Submitted Request")
    else:
        form = DeviceForm()
        context = {'form': form}
        return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        f = DeviceForm(request.POST)
        f.save()
        context = {'form': f}
        return render(request,'create.html', context)
    else:
        form = CreateDeviceForm()
        context={'form': form}
        return render(request, 'create.html', context)