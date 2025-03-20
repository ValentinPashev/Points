from django.db import models

from accounts.choices import BranchChoices, CommitteeChoices
from accounts.models import Profile
from events.models import Event

class EventReport(models.Model):
    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    organizers = models.ManyToManyField(
        Profile,
        related_name='organized_events'
    )

    prepared = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prepared_reports'
    )

    attended = models.ManyToManyField(
        Profile,
        related_name='attended_events',
        blank=True
    )

    participated_actively = models.ManyToManyField(
        Profile,
        related_name='active_participants',
        blank=True
    )

    number_of_days = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    points_for_organizers = models.IntegerField(default=0)
    points_for_prepared = models.IntegerField(default=0)
    points_for_attended = models.IntegerField(default=0)
    points_for_participated_actively = models.IntegerField(default=0)

    branch = models.CharField(
        max_length=100,
        choices=BranchChoices.choices,
        default=BranchChoices.ASMB_SU
    )

    committee = models.CharField(
        max_length=100,
        choices=CommitteeChoices.choices,
        default=CommitteeChoices.SCORA
    )

    def __str__(self):
        return f"Отчет за {self.event.name}"