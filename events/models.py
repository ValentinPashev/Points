from django.db import models

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


    def __str__(self):
        return self.name

