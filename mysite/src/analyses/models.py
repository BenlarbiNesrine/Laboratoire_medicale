from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
    # demande d'examen de prélèvement
class DemandeDexamen(models.Model):

    user                                   = models.ForeignKey(User , on_delete="None")
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_création_de_demande         = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
    Femme                                  = 'Femme'
    Homme                                  = 'Homme'
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

class CoproParasitologyResult(models.Model):

       user                                   = models.ForeignKey(User , on_delete="None")
       Nom_patient                            = models.CharField(max_length=40)
       Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
       Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
       Interne                                = 'Interne'
       Externe                                = 'Externe'
       SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
       Service                                = models.CharField(max_length=10 , choices=SERVICES ,default=Interne )
       Adresse                                = models.CharField(max_length=200 , default=None)
       Symptomes                              = models.CharField(max_length=500 ,default=None  )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       DOULEURS                               = [(Oui, 'Oui') , (Non, 'Non') ]
       Douleurs                               = models.CharField(max_length=3 , choices=DOULEURS ,default=Non)
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       DIARRHEE                               = [(Oui, 'Oui') , (Non, 'Non') ]
       Diarrhée                               = models.CharField(max_length=3 , choices=DIARRHEE ,default=Non )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       NAUSEES                                = [(Oui, 'Oui') , (Non, 'Non') ]
       Nausées                                = models.CharField(max_length=3 , choices=NAUSEES ,default=Non )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       VOMISSEMENT                            = [(Oui, 'Oui') , (Non, 'Non') ]
       Vomissement                            = models.CharField(max_length=3 , choices=VOMISSEMENT ,default=Non )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       BALLONNEMENT_ABDOMNAL                  = [(Oui, 'Oui') , (Non, 'Non') ]
       ballonnement_abdominal                 = models.CharField(max_length=3 , choices=BALLONNEMENT_ABDOMNAL ,default=Non )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       CONSTIPATION                           = [(Oui, 'Oui') , (Non, 'Non') ]
       Constipation                           = models.CharField(max_length=3 , choices= CONSTIPATION ,default=Non  )
       Oui                                    = 'Oui'
       Non                                    = 'Non'
       AMAIGRISSEMENT                         = [(Oui, 'Oui') , (Non, 'Non') ]
       Amaigrissement                         = models.CharField(max_length=3 , choices=AMAIGRISSEMENT ,default=Non   )
       Examen_Complémentaire                  = models.CharField(max_length=500 ,default=None  )
       Résultat                               = models.CharField(max_length=500 ,default=None  )
       Macroscopie                            = models.CharField(max_length=500 ,default=None  )
       Microscopie                            = models.CharField(max_length=500 ,default=None  )
       Etat_frais                             = models.CharField(max_length=500 ,default=None  )
       Ritchie                                = models.CharField(max_length=500 ,default=None  )
       Kato_Willis                            = models.CharField(max_length=500 ,default=None  )
       Scotch_test                            = models.CharField(max_length=500 ,default=None  )
       Autres                                 = models.CharField(max_length=1000 ,default=None)
       Autre                                  = models.CharField(max_length=1000 ,default=None)

    #Resultats du bilan d'urgence

class BilanDurgenceResult(models.Model):

      user                                   = models.ForeignKey(User , on_delete="None")
      Nom_patient                            = models.CharField(max_length=40)
      Horodatage_création_de_resultat         = models.DateTimeField(blank=True , default=datetime.datetime.now)
      Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
      Interne                                = 'Interne'
      Externe                                = 'Externe'
      SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
      Service                                = models.CharField(max_length=10 , choices=SERVICES )
      céphaline_kaolin                       = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
      INR                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
      prothrombine                           = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
      Glucose                                = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Urée                                   = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Créatinine                             = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      NA                                     = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      K                                      = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Calcium_ionisé                         = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      CRP                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Bilirubine_total                       = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Bilirubine_directe                     = models.DecimalField(max_digits=5, decimal_places=2, default=None)

       #Resultats du Biochimie

class BiochimieResult(models.Model):

  user                                   = models.ForeignKey(User , on_delete="None")
  Nom_patient                            = models.CharField(max_length=40)
  Horodatage_création_de_resultat         = models.DateTimeField(blank=True , default=datetime.datetime.now)
  Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
  Interne                                = 'Interne'
  Externe                                = 'Externe'
  SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
  Service                                = models.CharField(max_length=10 , choices=SERVICES )
  praticien                              = models.CharField(max_length=40)
  Glucose                                = models.DecimalField(max_digits=5 , decimal_places=2)
  Urée                                   = models.DecimalField(max_digits=5 , decimal_places=2)
  Créatinine                             = models.DecimalField(max_digits=5 , decimal_places=2)
  Acide_urique                           = models.DecimalField(max_digits=5 , decimal_places=2)
  Sodium                                 = models.DecimalField(max_digits=5 , decimal_places=2)
  Potasium                               = models.DecimalField(max_digits=5 , decimal_places=2)
  Calcium_total                          = models.DecimalField(max_digits=5 , decimal_places=2)
  Calcium_ionisé                         = models.DecimalField(max_digits=5 , decimal_places=2)
  Phosphore                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Magnésium                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Fer                                    = models.DecimalField(max_digits=5 , decimal_places=2)
  Aspect_du_sérum                        = models.DecimalField(max_digits=5 , decimal_places=2)
  Cholestérol_total                      = models.DecimalField(max_digits=5 , decimal_places=2)
  Triglycérides                          = models.DecimalField(max_digits=5 , decimal_places=2)
  HDL_Cholestérol                        = models.DecimalField(max_digits=5 , decimal_places=2)
  LDL_Cholestérol                        = models.DecimalField(max_digits=5 , decimal_places=2)
  Protéines                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Albumine                               = models.DecimalField(max_digits=5 , decimal_places=2)
  Amylase                                = models.DecimalField(max_digits=5 , decimal_places=2)
  Lipase                                 = models.DecimalField(max_digits=5 , decimal_places=2)
  CK_Homme                               = models.DecimalField(max_digits=5 , decimal_places=2)
  CK_Femme                               = models.DecimalField(max_digits=5 , decimal_places=2)
  CK_MB                                  = models.DecimalField(max_digits=5 , decimal_places=2)
  LDH                                    = models.DecimalField(max_digits=5 , decimal_places=2)
  GOT                                    = models.DecimalField(max_digits=5 , decimal_places=2)
  GPT                                    = models.DecimalField(max_digits=5 , decimal_places=2)
  y_gt_h                                 = models.DecimalField(max_digits=5 , decimal_places=2)
  y_gt_f                                 = models.DecimalField(max_digits=5 , decimal_places=2)
  Bilirubine_total                       = models.DecimalField(max_digits=5 , decimal_places=2)
  Bilirubine_directe                     = models.DecimalField(max_digits=5 , decimal_places=2)
  Bilirubine_indirecte                   = models.DecimalField(max_digits=5 , decimal_places=2)
  PAL_AMP                                = models.DecimalField(max_digits=5 , decimal_places=2)
  PAL_DEA                                = models.DecimalField(max_digits=5 , decimal_places=2)
  Diurèse                                = models.DecimalField(max_digits=5 , decimal_places=2)
  Protéines_ur                           = models.DecimalField(max_digits=5 , decimal_places=2)
  Microalbumine                          = models.DecimalField(max_digits=5 , decimal_places=2)
  Créatinine_ur                          = models.DecimalField(max_digits=5 , decimal_places=2)
  Clairance                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Urée_ur                                = models.DecimalField(max_digits=5 , decimal_places=2)
  Sodium_ur                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Potasium_ur                            = models.DecimalField(max_digits=5 , decimal_places=2)
  Calcium_ur                             = models.DecimalField(max_digits=5 , decimal_places=2)
  Phosphore_ur                           = models.DecimalField(max_digits=5 , decimal_places=2)
  Acide_urique_ur                        = models.DecimalField(max_digits=5 , decimal_places=2)
  Glucose_ur                             = models.DecimalField(max_digits=5 , decimal_places=2)
  Amylase_ur                             = models.DecimalField(max_digits=5 , decimal_places=2)

            #Resultats de Biochimie Min

class BiochimieMinResult(models.Model):

  user                                   = models.ForeignKey(User , on_delete="None")
  Nom_patient                            = models.CharField(max_length=40)
  Horodatage_création_de_resultat         = models.DateTimeField(blank=True , default=datetime.datetime.now)
  Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
  medecin                                = models.CharField(max_length=40, default=None)
  Interne                                = 'Interne'
  Externe                                = 'Externe'
  SERVICES                               = [(Interne, 'Interne') , (Externe, 'Externe') ]
  Service                                = models.CharField(max_length=10 , choices=SERVICES )
  Glucose                                = models.DecimalField(max_digits=5, decimal_places=2,default=None)
  Urée                                   = models.DecimalField(max_digits=5, decimal_places=2)
  Créatinine                             = models.DecimalField(max_digits=5, decimal_places=2)
  NA                                     = models.DecimalField(max_digits=5, decimal_places=2)
  K                                      = models.DecimalField(max_digits=5, decimal_places=2)
  CA                                     = models.DecimalField(max_digits=5, decimal_places=2)
  ALB                                    = models.DecimalField(max_digits=5, decimal_places=2)
