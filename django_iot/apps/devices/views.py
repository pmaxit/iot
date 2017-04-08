from django.shortcuts import render
from .forms import DeviceForm
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        print request
        return HttpResponse("Submitted Request")
    else:
        form = DeviceForm()
        context = {'form': form}
        return render(request, 'index.html', context)