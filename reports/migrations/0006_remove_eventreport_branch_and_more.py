# Generated by Django 5.1.6 on 2025-03-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reports",
            "0005_remove_eventreport_users_remove_eventreport_attended_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventreport",
            name="branch",
        ),
        migrations.RemoveField(
            model_name="eventreport",
            name="committee",
        ),
        migrations.AlterField(
            model_name="eventreport",
            name="points_for_attended",
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name="eventreport",
            name="points_for_organizers",
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name="eventreport",
            name="points_for_participated_actively",
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name="eventreport",
            name="points_for_prepared",
            field=models.IntegerField(default=5),
        ),
    ]
