# Generated by Django 4.2.3 on 2023-07-30 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_weather_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='favorite',
        ),
    ]
