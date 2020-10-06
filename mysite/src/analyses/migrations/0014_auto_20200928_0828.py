# Generated by Django 2.2 on 2020-09-28 07:28

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0013_auto_20200928_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilandurgenceresult',
            name='Service',
            field=models.CharField(choices=[('Externe', 'Externe'), ('Interne (COA)', 'Interne (COA)'), ('Interne (POA)', 'Interne (POA)'), ('Interne (COB)', 'Interne (COB)'), ('Interne (Curtillet)', 'Interne (Curtillet)'), ('Interne (Chir Plastique)', 'Interne (Chir Plastique)'), ('Interne (Chir Générale)', 'Interne (Chir Générale)'), ('Interne (CCI)', 'Interne (CCI)'), ('Interne (Chrurgie Maxito faciale)', 'Interne (Chrurgie Maxito faciale)'), ('Interne (Rea Med Rhu)', 'Interne (Rea Med Rhu)'), ('Interne (Med Interne)', 'Interne (Med Interne)'), ('Interne (Néonat)', 'Interne (Néonat)'), ('Interne (MTV)', 'Interne (MTV)'), ('Interne (PU T)', 'Interne (PU T)'), ('Interne (PU Chir)', 'Interne (PU Chir)'), ('Interne (PU MI)', 'Interne (PU MI)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='biochimieminresult',
            name='Service',
            field=models.CharField(choices=[('Externe', 'Externe'), ('Interne (COA)', 'Interne (COA)'), ('Interne (POA)', 'Interne (POA)'), ('Interne (COB)', 'Interne (COB)'), ('Interne (Curtillet)', 'Interne (Curtillet)'), ('Interne (Chir Plastique)', 'Interne (Chir Plastique)'), ('Interne (Chir Générale)', 'Interne (Chir Générale)'), ('Interne (CCI)', 'Interne (CCI)'), ('Interne (Chrurgie Maxito faciale)', 'Interne (Chrurgie Maxito faciale)'), ('Interne (Rea Med Rhu)', 'Interne (Rea Med Rhu)'), ('Interne (Med Interne)', 'Interne (Med Interne)'), ('Interne (Néonat)', 'Interne (Néonat)'), ('Interne (MTV)', 'Interne (MTV)'), ('Interne (PU T)', 'Interne (PU T)'), ('Interne (PU Chir)', 'Interne (PU Chir)'), ('Interne (PU MI)', 'Interne (PU MI)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='biochimieresult',
            name='Service',
            field=models.CharField(choices=[('Externe', 'Externe'), ('Interne (COA)', 'Interne (COA)'), ('Interne (POA)', 'Interne (POA)'), ('Interne (COB)', 'Interne (COB)'), ('Interne (Curtillet)', 'Interne (Curtillet)'), ('Interne (Chir Plastique)', 'Interne (Chir Plastique)'), ('Interne (Chir Générale)', 'Interne (Chir Générale)'), ('Interne (CCI)', 'Interne (CCI)'), ('Interne (Chrurgie Maxito faciale)', 'Interne (Chrurgie Maxito faciale)'), ('Interne (Rea Med Rhu)', 'Interne (Rea Med Rhu)'), ('Interne (Med Interne)', 'Interne (Med Interne)'), ('Interne (Néonat)', 'Interne (Néonat)'), ('Interne (MTV)', 'Interne (MTV)'), ('Interne (PU T)', 'Interne (PU T)'), ('Interne (PU Chir)', 'Interne (PU Chir)'), ('Interne (PU MI)', 'Interne (PU MI)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='coproparasitologyresult',
            name='Service',
            field=models.CharField(choices=[('Externe', 'Externe'), ('Interne (COA)', 'Interne (COA)'), ('Interne (POA)', 'Interne (POA)'), ('Interne (COB)', 'Interne (COB)'), ('Interne (Curtillet)', 'Interne (Curtillet)'), ('Interne (Chir Plastique)', 'Interne (Chir Plastique)'), ('Interne (Chir Générale)', 'Interne (Chir Générale)'), ('Interne (CCI)', 'Interne (CCI)'), ('Interne (Chrurgie Maxito faciale)', 'Interne (Chrurgie Maxito faciale)'), ('Interne (Rea Med Rhu)', 'Interne (Rea Med Rhu)'), ('Interne (Med Interne)', 'Interne (Med Interne)'), ('Interne (Néonat)', 'Interne (Néonat)'), ('Interne (MTV)', 'Interne (MTV)'), ('Interne (PU T)', 'Interne (PU T)'), ('Interne (PU Chir)', 'Interne (PU Chir)'), ('Interne (PU MI)', 'Interne (PU MI)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demandedexamen',
            name='Nature_examen',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Biochimie'), (2, 'Hémobiologie'), (3, 'Parasitologie-Mycologie'), (4, 'Microbiologie')], max_length=10),
        ),
    ]
