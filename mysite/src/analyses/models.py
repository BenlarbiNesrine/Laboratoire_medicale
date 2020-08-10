from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class DemandeDexamen(models.Model):

    user                                   = models.ForeignKey(User , on_delete="None")
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_création_de_demande         = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
    Femme                                  = 'Femme'
    Homme                                  = 'Himme'
    SEXE                                   = [(Femme, 'Femme') , (Homme, 'Homme') ]
    Sexe                                   = models.CharField(max_length=10 , choices=SEXE )
    Interne                                = 'Interne'
    Externe                                = 'Externe'
    SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
    Service                                = models.CharField(max_length=10 , choices=SERVICES )
    Médecin_prescripteur                   = models.CharField(max_length=40)
    Sang                                   = 'Sang'
    Urine                                  = 'Urine'
    LCR                                    = 'LCR'
    Liquide_d_acite                        = 'Liquide_d_acite'
    Selles                                 = 'Selles'
    Pus                                    = 'Pus'
    Hémoculture                            = 'Hémoculture'
    NATURE_DE_PRELEVEMENT                  = [(Sang, 'Sang') , (Urine, 'Urine') , (LCR, 'LCR') ,(Liquide_d_acite, 'Liquide_d_acite') ,
                                              (Selles, 'Selles') , (Pus, 'Pus') , (Hémoculture, 'Hémoculture') ]
    Nature_de_prelèvement                  = models.CharField(max_length=10 , choices=NATURE_DE_PRELEVEMENT    )
    Nombre_de_tubes                        = models.PositiveIntegerField( validators=[MaxValueValidator(5), MinValueValidator(1)] , default=1)
    Nature_des_tubes                       = models.TextField(blank = True)
    NONE                                   = 'NONE'
    Biochimie                              = 'Biochimie'
    Hemobiologie                           = 'Hémobiologie'
    Parasitologie_Mycologie                = 'Parasitologie-Mycologie'
    Microbiologie                          = 'Microbiologie'
    NATURE_D_EXAMEN                        = [(NONE, 'NONE') , (Biochimie, 'Biochimie') , (Hemobiologie, 'Hémobiologie') ,
                                              (Parasitologie_Mycologie, 'Parasitologie-Mycologie') , ( Microbiologie, 'Microbiologie') ]
    Nature_examen                          = models.CharField(max_length=10 , choices=NATURE_D_EXAMEN )
    Diagnostic                             = models.TextField(blank = True)


    def __str__(self):
        return self.Nom_patient




#result section

   #CoproParasitologyResult

#class CoproParasitologyResult(models.Model):

       #user                                   = models.ForeignKey(User , on_delete="None")
       #Nom_Patient                            = models.CharField(max_length=40)
       #Horodatage_création_de_demande         = models.DateTimeField(blank=True , default=datetime.datetime.now)
       #Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
       #Femme                                  = 'Femme'
       #Homme                                  = 'Himme'
       #SEXE                                   = [(Femme, 'Femme') , (Homme, 'Homme') ]
       #Sexe                                   = models.CharField(max_length=10 , choices=SEXE )
       #Interne                                = 'Interne'
       #Externe                                = 'Externe'
       #SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
       #Service                                = models.CharField(max_length=10 , choices=SERVICES )



    #def __str__(self):
        # return self.Nom_Patient
