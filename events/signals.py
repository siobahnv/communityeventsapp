from events.models import Event, Report, Sponsorship

from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.core.signals import post_save

@receiver(post_save, sender=Event)
def ensure_profile_exists(sender, **kwargs):
    print("Event created for reals!!!")
    if kwargs.get('created', False):
        print("Other events creaated!!!!!!!?")
        Report.objects.get_or_create(event=kwargs.get('instance'))
        Sponsorship.objects.get_or_create(event=kwargs.get('instance'))