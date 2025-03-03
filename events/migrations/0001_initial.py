# Generated by Django 5.1.6 on 2025-03-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Local', 'Local'), ('National', 'National')], default='Local', max_length=100)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
