from django.db import models

class TypeEventChoices(models.TextChoices):
    LOCAL = "Local", "Local"
    NATIONAL = "National", "National"