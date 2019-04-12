import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.

def index(request):
    events_list = Event.objects.all()
    context = {'events_list': events_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', { 'event': event})

# @login_required
def reports(request):
    reports_list = Report.objects.all()
    context = {'reports_list': reports_list}
    return render(request, 'events/reports.html', context)

def reports_detail(request, event_id):
    report = get_object_or_404(Report, pk=event_id)
    return render(request, 'events/reports_detail.html', { 'report': report})

def sponsorships(request):
    sponsorships_list = Sponsorship.objects.all()
    context = {'sponsorships_list': sponsorships_list}
    return render(request, 'events/sponsorships.html', context)

def sponsorships_detail(request, event_id):
    sponsorship = get_object_or_404(Sponsorship, pk=event_id)
    return render(request, 'events/sponsorships_detail.html', { 'sponsorship': sponsorship})

# @permission_required('')

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('events:index')
    # exclude = ('tags',)
    # initial = {}

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('events:index')

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('events:index')