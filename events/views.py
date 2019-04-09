from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import *

# Create your views here.

def index(request):
    events_list = Event.objects.all()
    context = {'events_list': events_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', { 'event': event})
