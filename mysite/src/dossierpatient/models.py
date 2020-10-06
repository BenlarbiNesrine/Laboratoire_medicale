from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.




class DossierPatient(models.Model):
  user                                   = models.ForeignKey(User , on_delete="None")
  Horodatage_creation_de_dossier         = models.DateTimeField(blank=True , default=datetime.datetime.now)
  nom_patient                            = models.CharField(max_length=40)
  Femme                                  = 'Femme'
  Homme                                  = 'Homme'
  SEXE                                   = [(Femme, 'Femme') , (Homme, 'Homme') ]
  sexe                                   = models.CharField(max_length=10 , choices=SEXE )
  date_de_naissance                      = models.DateField(auto_now=False, auto_now_add=False)

  class Meta:
      db_table = "DossierPatient"

  def __str__(self):
      return self.nom_patient
