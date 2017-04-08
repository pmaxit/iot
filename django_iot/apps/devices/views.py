from django.shortcuts import render
from .forms import DeviceForm
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