# Generated by Django 5.1.6 on 2025-03-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_profile_background_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="committee",
            field=models.CharField(
                choices=[
                    ("Scope", "Scope"),
                    ("Scora", "Scora"),
                    ("Score", "Score"),
                    ("Scome", "Scome"),
                    ("Scoph", "Scoph"),
                    ("Scopr", "Scopr"),
                ],
                default="Scora",
                max_length=100,
            ),
        ),
    ]
