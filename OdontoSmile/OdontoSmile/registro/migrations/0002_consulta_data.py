# Generated by Django 5.0.2 on 2024-08-08 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='data',
            field=models.DateField(default=datetime.datetime(2024, 8, 8, 18, 59, 30, 468571, tzinfo=datetime.timezone.utc)),
        ),
    ]
