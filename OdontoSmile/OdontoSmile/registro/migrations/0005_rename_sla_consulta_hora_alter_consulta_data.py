# Generated by Django 5.0.2 on 2024-08-08 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_consulta_sla_alter_consulta_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='sla',
            new_name='hora',
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(default=datetime.datetime(2024, 8, 8, 19, 7, 9, 124907, tzinfo=datetime.timezone.utc), verbose_name='data'),
        ),
    ]
