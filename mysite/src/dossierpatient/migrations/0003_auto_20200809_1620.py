# Generated by Django 2.2 on 2020-08-09 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossierpatient', '0002_auto_20200809_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossierpatient',
            name='horodatage_création_de_dossier',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
