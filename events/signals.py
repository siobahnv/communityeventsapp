from events.models import Event, Report, Sponsorship

from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.core.signals import post_save

@receiver(post_save, sender=Event)
def setup_new_event(sender, **kwargs):
    if kwargs.get('created', False):
        Report.objects.get_or_create(event=kwargs.get('instance'))
        Sponsorship.objects.get_or_create(event=kwargs.get('instance'))