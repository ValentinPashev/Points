from django.db import models

from accounts.choices import BranchChoices, CommitteeChoices
from accounts.models import Profile
from events.models import Event


# Create your models here.

class EventReport(models.Model):

    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        related_name='reports',)

    users = models.ManyToManyField(
        Profile,
    )

    number_of_days = models.IntegerField(
        default=0,
    )

    organizers = models.ManyToManyField(
        'accounts.Profile',
        related_name='organizers',
    )

    prepared = models.TextField(
        max_length=35,
        null=True,
        blank=True
    )

    attended = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

    participated_actively = models.TextField(
        max_length=350,
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    points_for_organizers = models.IntegerField(
        default=0
    )

    points_for_prepared = models.IntegerField(
        default=0
    )

    points_for_attended = models.IntegerField(
        default=0
    )

    points_for_participated_actively = models.IntegerField(
        default=0
    )

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