from django.db import models
from django.templatetags.static import static

from accounts.choices import BranchChoices, CommitteeChoices
from accounts.models import AppStudent, Profile
from events.choices import TypeEventChoices


# Create your models here.

class Event(models.Model):
    name = models.CharField(
        max_length=100
    )

    date = models.DateTimeField(

    )

    description = models.TextField(
        max_length=1000
    )

    location = models.CharField(
        max_length=100
    )

    type = models.CharField(
        max_length=100,
        choices=TypeEventChoices.choices,
        default=TypeEventChoices.LOCAL
    )

    approved = models.BooleanField(
        default=False
    )

    created_by = models.CharField(
        max_length=100,
    )

    branch = models.CharField(
        max_length=100,
        choices=BranchChoices.choices,
        default=BranchChoices.ASMB_SU
    )

    poster = models.ImageField(
        upload_to="media",
        blank=True,
        null=True,
    )

    committee = models.CharField(
        max_length=100,
        choices=CommitteeChoices.choices,
        default=CommitteeChoices.SCORA

    )

    def get_background_image(self):

        branch_images = {
            "АСМБ София": "universities/АСМБ София.jpg",
            "АСМБ СУ": "universities/АСМБ СУ.png",
            "АСМБ Варна": "universities/АСМБ Варна.jpg",
            "АСМ Пловдив": "universities/АСМ Пловдив.jpg",
            "АСМБ Бургас": "universities/АСМБ Бургас.jpg",
            "АСМБ Плевен": "universities/АСМБ Плевен.jpg",
            "АСМБ Стара Загора": "universities/АСМБ Стара Загора.jpg",
        }
        return static(branch_images.get(self.branch, "images/branches/default_bg.jpg"))

    def __str__(self):
        return self.name



class FavouriteEvent(models.Model):
    user = models.ForeignKey(
        AppStudent,
        on_delete=models.CASCADE,
        related_name="favourite_events",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="favourite_by",
    )

    class Meta:
        unique_together = ('user', 'event')