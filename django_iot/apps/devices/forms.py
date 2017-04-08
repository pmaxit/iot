from django import forms
from .models import Device

class DeviceForm(forms.Form):
    
    listDevices = Device.objects.all()
    Devices = forms.ChoiceField(choices=[(x, y) for x,y in enumerate(listDevices)])
    command = forms.ChoiceField(choices=[(x,y)  for x,y in enumerate(["on","off"])])