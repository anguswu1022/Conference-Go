# Generated by Django 4.0.3 on 2023-02-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='weather',
            field=models.TextField(default=''),
        ),
    ]
