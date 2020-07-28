from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class DossierPatient(models.Model):
  user                                   = models.ForeignKey(User , on_delete="None")
  nom_patient                            = models.CharField(max_length=40)
  sexe                                   = models.CharField(max_length=10)
  date_de_naissance                      = models.DateField(auto_now=False, auto_now_add=False)
  horodatage_création_de_dossier         = models.DateTimeField(blank=True , default=datetime.datetime.now)
#  tags                                  = models.CharField(max_length=40)

  def __str__(self):
      return self.nom_patient
