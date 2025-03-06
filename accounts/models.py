from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts.choices import BranchChoices
from django.utils.translation import gettext_lazy as _
from accounts.managers import AppStudentManager


class AppStudent(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,

    )

    username = models.CharField(
        max_length=30,
        unique=True,
    )

    faculty_number = models.CharField(
        max_length=25,
        unique=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    can_make_reports = models.BooleanField(
        default=False,
    )


    objects = AppStudentManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppStudent,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    branch = models.CharField(
        max_length=25,
        choices=BranchChoices.choices,
    )

    points_from_events = models.IntegerField(
        default=0
    )

    profile_picture = models.ImageField(
        upload_to="media",
        blank=True,
        null=True,
    )

    background_picture = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"