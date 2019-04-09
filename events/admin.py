from django.contrib import admin
from .models import Event, Report, Sponsorship, Tag

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'country', 'start_date', 'end_date', 'votes')

admin.site.register(Report)

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_filter = ('status', 'action_by', 'event_rating')

admin.site.register(Tag)
