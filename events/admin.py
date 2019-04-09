from django.contrib import admin
from .models import Event, Report, Sponsorship

# Register your models here.
admin.site.register(Event)
admin.site.register(Report)
admin.site.register(Sponsorship)
