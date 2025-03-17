# Generated by Django 5.1.6 on 2025-03-17 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0004_appstudent_can_approve_events"),
        ("events", "0004_event_completed"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_days", models.IntegerField(default=0)),
                ("organizers", models.TextField(blank=True, max_length=100, null=True)),
                ("prepared", models.TextField(blank=True, max_length=35, null=True)),
                ("attended", models.TextField(blank=True, max_length=1000, null=True)),
                (
                    "participated_actively",
                    models.TextField(blank=True, max_length=350, null=True),
                ),
                ("completed", models.BooleanField(default=False)),
                ("points_for_organizers", models.IntegerField(default=0)),
                ("points_for_prepared", models.IntegerField(default=0)),
                ("points_for_attended", models.IntegerField(default=0)),
                ("points_for_participated_actively", models.IntegerField(default=0)),
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="events.event",
                    ),
                ),
                ("users", models.ManyToManyField(to="accounts.profile")),
            ],
        ),
    ]
