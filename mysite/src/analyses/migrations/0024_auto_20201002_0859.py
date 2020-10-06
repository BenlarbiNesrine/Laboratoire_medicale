# Generated by Django 2.2 on 2020-10-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0023_auto_20201001_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='HCT',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='HGB',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='LYM',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='MCH',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='MCHC',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='MCV',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='NEUT',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='PLT',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='RBC',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='WBC',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='CRP',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
    ]
