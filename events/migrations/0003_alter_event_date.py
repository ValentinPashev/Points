# Generated by Django 5.1.6 on 2025-03-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
