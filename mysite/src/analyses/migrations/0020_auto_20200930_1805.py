# Generated by Django 2.2 on 2020-09-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0019_auto_20200929_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilandurgenceresult',
            name='Cas_d_erreur',
            field=models.CharField(choices=[('Prélèvement non conforme', 'Prélèvement non conforme'), ("Erreur d'étiquetage", "Erreur d'étiquetage"), ("Panne technique de l'automate", "Panne technique de l'automate"), ('Prélèvement non acheminé', 'Prélèvement non acheminé'), ('Défaut de prescription du médecin', 'Défaut de prescription du médecin'), ('Réactif non disponible à la pharmacie', 'Réactif non disponible à la pharmacie')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieminresult',
            name='Cas_d_erreur',
            field=models.CharField(choices=[('Prélèvement non conforme', 'Prélèvement non conforme'), ("Erreur d'étiquetage", "Erreur d'étiquetage"), ("Panne technique de l'automate", "Panne technique de l'automate"), ('Prélèvement non acheminé', 'Prélèvement non acheminé'), ('Défaut de prescription du médecin', 'Défaut de prescription du médecin'), ('Réactif non disponible à la pharmacie', 'Réactif non disponible à la pharmacie')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biochimieresult',
            name='Cas_d_erreur',
            field=models.CharField(choices=[('Prélèvement non conforme', 'Prélèvement non conforme'), ("Erreur d'étiquetage", "Erreur d'étiquetage"), ("Panne technique de l'automate", "Panne technique de l'automate"), ('Prélèvement non acheminé', 'Prélèvement non acheminé'), ('Défaut de prescription du médecin', 'Défaut de prescription du médecin'), ('Réactif non disponible à la pharmacie', 'Réactif non disponible à la pharmacie')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coproparasitologyresult',
            name='Cas_d_erreur',
            field=models.CharField(choices=[('Prélèvement non conforme', 'Prélèvement non conforme'), ("Erreur d'étiquetage", "Erreur d'étiquetage"), ("Panne technique de l'automate", "Panne technique de l'automate"), ('Prélèvement non acheminé', 'Prélèvement non acheminé'), ('Défaut de prescription du médecin', 'Défaut de prescription du médecin'), ('Réactif non disponible à la pharmacie', 'Réactif non disponible à la pharmacie')], max_length=10),
        ),
    ]
