from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the events index.")
    events_list = Event.objects.all()
    template = loader.get_template('events/index.html')
    context = {
        'events_list': events_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)
