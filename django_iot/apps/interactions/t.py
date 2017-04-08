from django.utils import timezone
#from django_iot.apps.devices.models import Device
from celery import Celery
import os

app = Celery("tasks", backend ='amqp', broker='amqp://puneet:password@52.36.59. 156/myhost')

@app.task
def myTask(**kwargs):
    return "It Worked"
