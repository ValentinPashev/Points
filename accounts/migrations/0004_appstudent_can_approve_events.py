# Generated by Django 5.1.6 on 2025-03-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_profile_committee"),
    ]

    operations = [
        migrations.AddField(
            model_name="appstudent",
            name="can_approve_events",
            field=models.BooleanField(default=False),
        ),
    ]
