from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Event
from reports.models import EventReport


@receiver(post_save, sender=Event)
def create_event_report(sender, instance, created, **kwargs):
    if created:
        EventReport.objects.create(event=instance)