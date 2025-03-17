# Generated by Django 5.1.6 on 2025-03-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_appstudent_can_approve_events"),
        ("reports", "0002_eventreport_branch_eventreport_committee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventreport",
            name="organizers",
        ),
        migrations.AddField(
            model_name="eventreport",
            name="organizers",
            field=models.ManyToManyField(
                related_name="organizers", to="accounts.profile"
            ),
        ),
    ]
