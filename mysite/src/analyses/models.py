from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from dossierpatient.models import DossierPatient

# Create your models here.
    # demande d'examen de prélèvement
class DemandeDexamen(models.Model):
    dossier_patient                        = models.ForeignKey(DossierPatient, on_delete=models.CASCADE)
    user                                   = models.ForeignKey(User , on_delete="None")
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_création_de_demande         = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
    Femme                                  = 'Femme'
    Homme                                  = 'Homme'
    SEXE                                   = [(Femme, 'Femme') , (Homme, 'Homme') ]
    Sexe                                   = models.CharField(max_length=10 , choices=SEXE )
    Externe                                = 'Externe'
    Interne_COA                            = 'Interne (COA)'
    Interne_POA                            = 'Interne (POA)'
    Interne_COB                            = 'Interne (COB)'
    Interne_Curtillet                      = 'Interne (Curtillet)'
    Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
    Interne_Chir_Générale                  = 'Interne (Chir Générale)'
    Interne_CCI                            = 'Interne (CCI)'
    Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
    Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
    Interne_Med_Interne                    = 'Interne (Med Interne)'
    Interne_Néonat                         = 'Interne (Néonat)'
    Interne_MTV                            = 'Interne (MTV)'
    Interne_PU_T                           = 'Interne (PU T)'
    Interne_PU_Chir                        = 'Interne (PU Chir)'
    Interne_PU_MI                          = 'Interne (PU MI)'
    SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                                (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                                (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                                (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                                (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
    Service                                = models.CharField(max_length=10 , choices=SERVICES )
    Médecin_prescripteur                   = models.CharField(max_length=40)
    Sec                                    = 'Sec'
    Citrate                                = 'Citrate'
    Heparine                               = 'Heparine'
    EDTA                                   = 'EDTA'
    NATURE_DE_TUBE                         = [(Sec, 'Sec') , (Citrate, 'Citrate') , (Heparine, 'Heparine') ,(EDTA, 'EDTA')]
    Nature_de_tube                         = models.CharField(max_length=10 , choices=NATURE_DE_TUBE    )
    Nombre_de_tubes                        = models.PositiveIntegerField( validators=[MaxValueValidator(5), MinValueValidator(1)] , default=1)
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
    examen_choices                         = ((1,'Biochimie'),(2,'Hémobiologie'),(3,'Parasitologie-Mycologie') ,  (4,'Microbiologie'))
    Nature_examen                          = MultiSelectField(max_length=10 , choices=examen_choices)
    Diagnostic                             = models.TextField(blank = True)
    Symptomes                              = models.CharField(max_length=500 ,default=None  )
    Oui                                    = 'Oui'
    Non                                    = 'Non'
    choix                                  = [(Oui, 'Oui') , (Non, 'Non') ]
    Douleurs                               = models.CharField(max_length=3 , choices=choix ,default=Non)
    Diarrhée                               = models.CharField(max_length=3 , choices=choix ,default=Non )
    Nausées                                = models.CharField(max_length=3 , choices=choix ,default=Non )
    Vomissement                            = models.CharField(max_length=3 , choices=choix ,default=Non )
    ballonnement_abdominal                 = models.CharField(max_length=3 , choices=choix ,default=Non )
    Fievre                                 = models.CharField(max_length=3 , choices=choix ,default=Non )
    diabete                                 = models.CharField(max_length=3 , choices=choix ,default=Non )
    Constipation                           = models.CharField(max_length=3 , choices=choix ,default=Non  )
    Amaigrissement                         = models.CharField(max_length=3 , choices=choix ,default=Non   )
    Examen_Complémentaire                  = models.CharField(max_length=500 ,default=None  )
    Autre                                  = models.CharField(max_length=1000 ,default=None)



    class Meta:
        db_table = "DemandeDexamen"

    def __str__(self):
        return self.Nom_patient



#result section

   #CoproParasitologyResult

class CoproParasitologyResult(models.Model):
       demande_CP                             = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
       user                                   = models.ForeignKey(User , on_delete="None")
       Nom_patient                            = models.CharField(max_length=40)
       Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
       Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
       Externe                                = 'Externe'
       Interne_COA                            = 'Interne (COA)'
       Interne_POA                            = 'Interne (POA)'
       Interne_COB                            = 'Interne (COB)'
       Interne_Curtillet                      = 'Interne (Curtillet)'
       Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
       Interne_Chir_Générale                  = 'Interne (Chir Générale)'
       Interne_CCI                            = 'Interne (CCI)'
       Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
       Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
       Interne_Med_Interne                    = 'Interne (Med Interne)'
       Interne_Néonat                         = 'Interne (Néonat)'
       Interne_MTV                            = 'Interne (MTV)'
       Interne_PU_T                           = 'Interne (PU T)'
       Interne_PU_Chir                        = 'Interne (PU Chir)'
       Interne_PU_MI                          = 'Interne (PU MI)'
       SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                                   (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                                   (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                                   (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                                   (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
       Service                                = models.CharField(max_length=10 , choices=SERVICES )
       Adresse                                = models.CharField(max_length=200 , default=None)
       Résultat                               = models.CharField(max_length=500 ,default=None  )
       Macroscopie                            = models.CharField(max_length=500 ,default=None  )
       Microscopie                            = models.CharField(max_length=500 ,default=None  )
       Etat_frais                             = models.CharField(max_length=500 ,default=None  )
       Ritchie                                = models.CharField(max_length=500 ,default=None  )
       Kato_Willis                            = models.CharField(max_length=500 ,default=None  )
       Scotch_test                            = models.CharField(max_length=500 ,default=None  )
       Autres                                 = models.CharField(max_length=1000 ,default=None)
       Prélèvement_non_conforme               = 'Prélèvement non conforme'
       Erreur_détiquetage                     = 'Erreur d\'étiquetage'
       Prélèvement_non_acheminé               ='Prélèvement non acheminé'
       Défaut_de_prescription_du_médecin      ='Défaut de prescription du médecin'
       Panne_technique_de_lautomate           ='Panne technique de l\'automate'
       Réactif_non_disponible_à_la_pharmacie  ='Réactif non disponible à la pharmacie'
       ERREUR                                 = [ (Prélèvement_non_conforme, 'Prélèvement non conforme'), (Erreur_détiquetage,'Erreur d\'étiquetage'), (Panne_technique_de_lautomate,'Panne technique de l\'automate'),(Prélèvement_non_acheminé, 'Prélèvement non acheminé'), (Défaut_de_prescription_du_médecin, 'Défaut de prescription du médecin'), (Réactif_non_disponible_à_la_pharmacie, 'Réactif non disponible à la pharmacie') ]
       Cas_d_erreur                           = models.CharField(max_length=10 , choices=ERREUR )

       class Meta:
           db_table = "CoproParasitologyResult"

       def __str__(self):
           return self.Nom_patient
    #Resultats du bilan d'urgence

class BilanDurgenceResult(models.Model):
      demande_BU                             = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
      user                                   = models.ForeignKey(User , on_delete="None")
      Nom_patient                            = models.CharField(max_length=40)
      Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
      Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
      Externe                                = 'Externe'
      Interne_COA                            = 'Interne (COA)'
      Interne_POA                            = 'Interne (POA)'
      Interne_COB                            = 'Interne (COB)'
      Interne_Curtillet                      = 'Interne (Curtillet)'
      Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
      Interne_Chir_Générale                  = 'Interne (Chir Générale)'
      Interne_CCI                            = 'Interne (CCI)'
      Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
      Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
      Interne_Med_Interne                    = 'Interne (Med Interne)'
      Interne_Néonat                         = 'Interne (Néonat)'
      Interne_MTV                            = 'Interne (MTV)'
      Interne_PU_T                           = 'Interne (PU T)'
      Interne_PU_Chir                        = 'Interne (PU Chir)'
      Interne_PU_MI                          = 'Interne (PU MI)'
      SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                                  (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                                  (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                                  (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                                  (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
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
      Prélèvement_non_conforme               = 'Prélèvement non conforme'
      Erreur_détiquetage                     = 'Erreur d\'étiquetage'
      Prélèvement_non_acheminé               ='Prélèvement non acheminé'
      Défaut_de_prescription_du_médecin      ='Défaut de prescription du médecin'
      Panne_technique_de_lautomate           ='Panne technique de l\'automate'
      Réactif_non_disponible_à_la_pharmacie  ='Réactif non disponible à la pharmacie'
      ERREUR                                 = [ (Prélèvement_non_conforme, 'Prélèvement non conforme'), (Erreur_détiquetage,'Erreur d\'étiquetage'), (Panne_technique_de_lautomate,'Panne technique de l\'automate'),(Prélèvement_non_acheminé, 'Prélèvement non acheminé'), (Défaut_de_prescription_du_médecin, 'Défaut de prescription du médecin'), (Réactif_non_disponible_à_la_pharmacie, 'Réactif non disponible à la pharmacie') ]
      Cas_d_erreur                           = models.CharField(max_length=10 , choices=ERREUR )
      WBC                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      RBC                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      HGB                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      HCT                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      MCV                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      MCH                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      MCHC                                   = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      PLT                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      LYM                                    = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      NEUT                                   = models.DecimalField(max_digits=5, decimal_places=2, default=None)
      Troponine                              = models.DecimalField(max_digits=5 , decimal_places=2)

      class Meta:
          db_table = "BilanDurgenceResult"

      def __str__(self):
          return self.Nom_patient
       #Resultats du Biochimie

class BiochimieResult(models.Model):
  demande_B                              = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
  user                                   = models.ForeignKey(User , on_delete="None")
  Nom_patient                            = models.CharField(max_length=40)
  Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
  Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
  Externe                                = 'Externe'
  Interne_COA                            = 'Interne (COA)'
  Interne_POA                            = 'Interne (POA)'
  Interne_COB                            = 'Interne (COB)'
  Interne_Curtillet                      = 'Interne (Curtillet)'
  Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
  Interne_Chir_Générale                  = 'Interne (Chir Générale)'
  Interne_CCI                            = 'Interne (CCI)'
  Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
  Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
  Interne_Med_Interne                    = 'Interne (Med Interne)'
  Interne_Néonat                         = 'Interne (Néonat)'
  Interne_MTV                            = 'Interne (MTV)'
  Interne_PU_T                           = 'Interne (PU T)'
  Interne_PU_Chir                        = 'Interne (PU Chir)'
  Interne_PU_MI                          = 'Interne (PU MI)'
  SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                              (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                              (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                              (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                              (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
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
  CRP                                    = models.DecimalField(max_digits=5 , decimal_places=2)
  Femme                                  = 'Clair'
  Homme                                  = 'Clairr'
  aspect_du_sérum                        = [(Femme, 'Clair') , (Homme, 'Clairr') ]

  Aspect_du_sérum                        = models.CharField(max_length=10 , choices=aspect_du_sérum )
  HBA1C                                  = models.DecimalField(max_digits=5 , decimal_places=2)
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
  Troponine                              = models.DecimalField(max_digits=5 , decimal_places=2)
  Prélèvement_non_conforme               = 'Prélèvement non conforme'
  Erreur_détiquetage                     = 'Erreur d\'étiquetage'
  Prélèvement_non_acheminé               ='Prélèvement non acheminé'
  Défaut_de_prescription_du_médecin      ='Défaut de prescription du médecin'
  Panne_technique_de_lautomate           ='Panne technique de l\'automate'
  Réactif_non_disponible_à_la_pharmacie  ='Réactif non disponible à la pharmacie'
  ERREUR                                 = [ (Prélèvement_non_conforme, 'Prélèvement non conforme'), (Erreur_détiquetage,'Erreur d\'étiquetage'), (Panne_technique_de_lautomate,'Panne technique de l\'automate'),(Prélèvement_non_acheminé, 'Prélèvement non acheminé'), (Défaut_de_prescription_du_médecin, 'Défaut de prescription du médecin'), (Réactif_non_disponible_à_la_pharmacie, 'Réactif non disponible à la pharmacie') ]
  Cas_d_erreur                           = models.CharField(max_length=10 , choices=ERREUR )

  class Meta:
      db_table = "BiochimieResult"

  def __str__(self):
      return self.Nom_patient

     #hemobiologie
  #groupage sanguin

class GroupageSanguin(models.Model):
    user                                   = models.ForeignKey(User , on_delete="None")
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_creation_de_groupage        = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Adresse                                = models.CharField(max_length=200 , default=None)
    A                                      = 'A'
    B                                      = 'B'
    AB                                     = 'AB'
    O                                      = 'O'
    GROUPE                                 = [(A, 'A') , (B, 'B'), (AB, 'AB'), (O, 'O') ]
    Groupe                                 = models.CharField(max_length=10 , choices=GROUPE )
    Positive                               = '+'
    Négative                               = '-'
    RH                                     = [(Positive, '+') , (Négative, '-')]
    Rh                                     = models.CharField(max_length=10 , choices=RH )
    class Meta:
       db_table = "GroupageSanguin"

    def __str__(self):
        return self.Nom_patient


              #FNS ET HEMOSTASE


          #Microbiologie (bactériologie)
        #Antibiogrammepour acinetobacter

class AcinetobacterResult(models.Model):
  user                                   = models.ForeignKey(User , on_delete="None")
  demande_ACIN                           = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
  Nom_patient                            = models.CharField(max_length=40)
  Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
  Référence                              = models.CharField(max_length=200 , default=None)
  Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
  Externe                                = 'Externe'
  Interne_COA                            = 'Interne (COA)'
  Interne_POA                            = 'Interne (POA)'
  Interne_COB                            = 'Interne (COB)'
  Interne_Curtillet                      = 'Interne (Curtillet)'
  Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
  Interne_Chir_Générale                  = 'Interne (Chir Générale)'
  Interne_CCI                            = 'Interne (CCI)'
  Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
  Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
  Interne_Med_Interne                    = 'Interne (Med Interne)'
  Interne_Néonat                         = 'Interne (Néonat)'
  Interne_MTV                            = 'Interne (MTV)'
  Interne_PU_T                           = 'Interne (PU T)'
  Interne_PU_Chir                        = 'Interne (PU Chir)'
  Interne_PU_MI                          = 'Interne (PU MI)'
  SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                              (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                              (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                              (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                              (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
  Service                                = models.CharField(max_length=10 , choices=SERVICES )
  praticien                              = models.CharField(max_length=40)
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
  Examen_Directe                         = models.CharField(max_length=500)
  Germe_isolé                            = models.CharField(max_length=500)
  Observation                            = models.CharField(max_length=1000)
  class Meta:
     db_table = "AcinetobacterResult"

  def __str__(self):
      return self.Nom_patient


    #Antibiogramme pour entérocoque

class EnterocoqueResult(models.Model):
    user                                   = models.ForeignKey(User , on_delete="None")
    demande_Ente                           = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Référence                              = models.CharField(max_length=200 , default=None)
    Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
    Externe                                = 'Externe'
    Interne_COA                            = 'Interne (COA)'
    Interne_POA                            = 'Interne (POA)'
    Interne_COB                            = 'Interne (COB)'
    Interne_Curtillet                      = 'Interne (Curtillet)'
    Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
    Interne_Chir_Générale                  = 'Interne (Chir Générale)'
    Interne_CCI                            = 'Interne (CCI)'
    Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
    Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
    Interne_Med_Interne                    = 'Interne (Med Interne)'
    Interne_Néonat                         = 'Interne (Néonat)'
    Interne_MTV                            = 'Interne (MTV)'
    Interne_PU_T                           = 'Interne (PU T)'
    Interne_PU_Chir                        = 'Interne (PU Chir)'
    Interne_PU_MI                          = 'Interne (PU MI)'
    SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                              (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                              (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                              (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                              (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
    Service                                = models.CharField(max_length=10 , choices=SERVICES )
    praticien                              = models.CharField(max_length=40)
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
    Examen_Directe                         = models.CharField(max_length=500)
    Germe_isolé                            = models.CharField(max_length=500)
    Observation                            = models.CharField(max_length=1000)
    class Meta:
     db_table = "EnterocoqueResult"

    def __str__(self):
      return self.Nom_patient


    #Antibiogramme pour Enterobacteries

class EnterobacteriesResult(models.Model):
    user                                   = models.ForeignKey(User , on_delete="None")
    demande_entero                         = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
    Nom_patient                            = models.CharField(max_length=40)
    Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
    Référence                              = models.CharField(max_length=200 , default=None)
    Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
    Externe                                = 'Externe'
    Interne_COA                            = 'Interne (COA)'
    Interne_POA                            = 'Interne (POA)'
    Interne_COB                            = 'Interne (COB)'
    Interne_Curtillet                      = 'Interne (Curtillet)'
    Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
    Interne_Chir_Générale                  = 'Interne (Chir Générale)'
    Interne_CCI                            = 'Interne (CCI)'
    Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
    Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
    Interne_Med_Interne                    = 'Interne (Med Interne)'
    Interne_Néonat                         = 'Interne (Néonat)'
    Interne_MTV                            = 'Interne (MTV)'
    Interne_PU_T                           = 'Interne (PU T)'
    Interne_PU_Chir                        = 'Interne (PU Chir)'
    Interne_PU_MI                          = 'Interne (PU MI)'
    SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                              (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                              (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                              (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                              (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
    Service                                = models.CharField(max_length=10 , choices=SERVICES )
    praticien                              = models.CharField(max_length=40)
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
    Examen_Directe                         = models.CharField(max_length=500)
    Germe_isolé                            = models.CharField(max_length=500)
    Observation                            = models.CharField(max_length=1000)
    class Meta:
     db_table = "EnterobacteriesResult"

    def __str__(self):
      return self.Nom_patient

           #Antibiogramme pour StaphylocoqueResult

class StaphylocoqueResult(models.Model):
   user                                   = models.ForeignKey(User , on_delete="None")
   demande_Staphy                         = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
   Nom_patient                            = models.CharField(max_length=40)
   Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
   Référence                              = models.CharField(max_length=200 , default=None)
   Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
   Externe                                = 'Externe'
   Interne_COA                            = 'Interne (COA)'
   Interne_POA                            = 'Interne (POA)'
   Interne_COB                            = 'Interne (COB)'
   Interne_Curtillet                      = 'Interne (Curtillet)'
   Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
   Interne_Chir_Générale                  = 'Interne (Chir Générale)'
   Interne_CCI                            = 'Interne (CCI)'
   Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
   Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
   Interne_Med_Interne                    = 'Interne (Med Interne)'
   Interne_Néonat                         = 'Interne (Néonat)'
   Interne_MTV                            = 'Interne (MTV)'
   Interne_PU_T                           = 'Interne (PU T)'
   Interne_PU_Chir                        = 'Interne (PU Chir)'
   Interne_PU_MI                          = 'Interne (PU MI)'
   SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                             (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                             (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                             (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                             (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
   Service                                = models.CharField(max_length=10 , choices=SERVICES )
   praticien                              = models.CharField(max_length=40)
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
   Examen_Directe                         = models.CharField(max_length=500)
   Germe_isolé                            = models.CharField(max_length=500)
   Observation                            = models.CharField(max_length=1000)
   class Meta:
    db_table = "StaphylocoqueResult"

   def __str__(self):
     return self.Nom_patient

           #Antibiogramme pour PseudomonasResult

class PseudomonasResult(models.Model):
   user                                   = models.ForeignKey(User , on_delete="None")
   demande_Pseu                           = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
   Nom_patient                            = models.CharField(max_length=40)
   Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
   Référence                              = models.CharField(max_length=200 , default=None)
   Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
   Externe                                = 'Externe'
   Interne_COA                            = 'Interne (COA)'
   Interne_POA                            = 'Interne (POA)'
   Interne_COB                            = 'Interne (COB)'
   Interne_Curtillet                      = 'Interne (Curtillet)'
   Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
   Interne_Chir_Générale                  = 'Interne (Chir Générale)'
   Interne_CCI                            = 'Interne (CCI)'
   Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
   Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
   Interne_Med_Interne                    = 'Interne (Med Interne)'
   Interne_Néonat                         = 'Interne (Néonat)'
   Interne_MTV                            = 'Interne (MTV)'
   Interne_PU_T                           = 'Interne (PU T)'
   Interne_PU_Chir                        = 'Interne (PU Chir)'
   Interne_PU_MI                          = 'Interne (PU MI)'
   SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                             (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                             (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                             (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                             (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
   Service                                = models.CharField(max_length=10 , choices=SERVICES )
   praticien                              = models.CharField(max_length=40)
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
   Examen_Directe                         = models.CharField(max_length=500)
   Germe_isolé                            = models.CharField(max_length=500)
   Observation                            = models.CharField(max_length=1000)
   class Meta:
    db_table = "PseudomonasResult"

   def __str__(self):
     return self.Nom_patient


           #BacteriologieResult

class BacteriologieResult(models.Model):
   user                                   = models.ForeignKey(User , on_delete="None")
   demande_Bact                           = models.ForeignKey('DemandeDexamen', on_delete=models.CASCADE)
   Nom_patient                            = models.CharField(max_length=40)
   Horodatage_création_de_resultat        = models.DateTimeField(blank=True , default=datetime.datetime.now)
   Référence                              = models.CharField(max_length=200 , default=None)
   Age                                    = models.PositiveIntegerField( validators=[MaxValueValidator(200), MinValueValidator(1)])
   Externe                                = 'Externe'
   Interne_COA                            = 'Interne (COA)'
   Interne_POA                            = 'Interne (POA)'
   Interne_COB                            = 'Interne (COB)'
   Interne_Curtillet                      = 'Interne (Curtillet)'
   Interne_Chir_Plastique                 = 'Interne (Chir Plastique)'
   Interne_Chir_Générale                  = 'Interne (Chir Générale)'
   Interne_CCI                            = 'Interne (CCI)'
   Interne_Chrurgie_Maxito_faciale        = 'Interne (Chrurgie Maxito faciale)'
   Interne_Rea_Med_Rhu                    = 'Interne (Rea Med Rhu)'
   Interne_Med_Interne                    = 'Interne (Med Interne)'
   Interne_Néonat                         = 'Interne (Néonat)'
   Interne_MTV                            = 'Interne (MTV)'
   Interne_PU_T                           = 'Interne (PU T)'
   Interne_PU_Chir                        = 'Interne (PU Chir)'
   Interne_PU_MI                          = 'Interne (PU MI)'
   SERVICES                               = [ (Externe, 'Externe') ,(Interne_COA, 'Interne (COA)') ,(Interne_POA,'Interne (POA)'),
                                             (Interne_COB,'Interne (COB)'),(Interne_Curtillet,'Interne (Curtillet)'),(Interne_Chir_Plastique,'Interne (Chir Plastique)'),
                                             (Interne_Chir_Générale,'Interne (Chir Générale)'),(Interne_CCI,'Interne (CCI)'),(Interne_Chrurgie_Maxito_faciale,'Interne (Chrurgie Maxito faciale)'),
                                             (Interne_Rea_Med_Rhu,'Interne (Rea Med Rhu)'),(Interne_Med_Interne,'Interne (Med Interne)'),(Interne_Néonat,'Interne (Néonat)'),
                                             (Interne_MTV,'Interne (MTV)'),(Interne_PU_T,'Interne (PU T)'),(Interne_PU_Chir,'Interne (PU Chir)'),(Interne_PU_MI,'Interne (PU MI)')]
   Service                                = models.CharField(max_length=10 , choices=SERVICES )
   praticien                              = models.CharField(max_length=40)
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
   Cytologie                              = models.CharField(max_length=500)
   Culture                                = models.CharField(max_length=500)

   class Meta:
    db_table = "BacteriologieResult"

   def __str__(self):
     return self.Nom_patient
