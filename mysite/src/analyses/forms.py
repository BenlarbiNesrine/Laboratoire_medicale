from django import forms
from .models import DemandeDexamen
from .models import CoproParasitologyResult
from .models import BilanDurgenceResult
from .models import BiochimieResult
from .models import BiochimieMinResult


class DemandeDexamenForm(forms.ModelForm):
    class Meta:
        model   = DemandeDexamen
        fields  = ['Horodatage_création_de_demande' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_des_tubes' ,"Nombre_de_tubes"   ,
                   'Nature_examen' ,'Diagnostic'  ]

class EditDemandeDexamForm(forms.ModelForm):
    class Meta:
        model   = DemandeDexamen
        fields  = ['Horodatage_création_de_demande' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_des_tubes' ,"Nombre_de_tubes"   ,
                   'Nature_examen' ,'Diagnostic'  ]
    class Meta:
        model   = DemandeDexamen
        fields  = ['Horodatage_création_de_demande' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_des_tubes' ,"Nombre_de_tubes"   ,
                   'Nature_examen' ,'Diagnostic'  ]

class DemandeDexamenSearchForm(forms.ModelForm):
      class Meta:
            model = DemandeDexamen
            fields = ['Nom_patient']
#result section
   #CoproParasitologyResult

class CoproParasitologyResultForm(forms.ModelForm):
    class Meta:
        model   = CoproParasitologyResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service' ,
                   'Adresse' , 'Symptomes' , 'Douleurs' , 'Diarrhée' , 'Examen_Complémentaire' ,
                   'Nausées' , 'Vomissement' , 'ballonnement_abdominal' , 'Constipation' ,
                   'Amaigrissement' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' , 'Autre', 'Autres']

class EditCoproParasitologyResultForm(forms.ModelForm):
    class Meta:
        model   = CoproParasitologyResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service' ,
                   'Adresse' , 'Symptomes' , 'Douleurs' , 'Diarrhée' , 'Examen_Complémentaire' ,
                   'Nausées' , 'Vomissement' , 'ballonnement_abdominal' , 'Constipation' ,
                   'Amaigrissement' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' , 'Autre', 'Autres']

  #Resultats du Bilan D'Urgence

class BilanDurgenceResultForm(forms.ModelForm):
    class Meta:
        model   = BilanDurgenceResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service','céphaline_kaolin','INR',
                   'prothrombine' ,'Glucose' , 'Urée', 'Créatinine', 'NA', 'K', 'Calcium_ionisé','CRP','Bilirubine_directe', 'Bilirubine_total']

class  EditBilanDurgenceResultForm(forms.ModelForm):
    class Meta:
        model   = BilanDurgenceResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service', 'céphaline_kaolin', 'INR',
                   'prothrombine' , 'Glucose' , 'Urée', 'Créatinine', 'NA','K','Calcium_ionisé', 'CRP', 'Bilirubine_directe', 'Bilirubine_total']

    #Resultats du Biochimie

class BiochimieResultForm(forms.ModelForm):
      class Meta:
          model   = BiochimieResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service','praticien', 'Glucose' ,'Urée', 'Créatinine',
                     'Acide_urique', 'Sodium', 'Potasium', 'Calcium_total', 'Calcium_ionisé', 'Phosphore', 'Magnésium', 'Fer',
                     'Aspect_du_sérum', 'Cholestérol_total', 'Triglycérides', 'HDL_Cholestérol', 'LDL_Cholestérol', 'Protéines',
                     'Albumine','Amylase', 'Lipase', 'CK_Homme' ,'CK_Femme','CK_MB', 'LDH' , 'GOT' , 'GPT', 'y_gt_h' ,'y_gt_f',
                     'Bilirubine_total' , 'Bilirubine_directe' , 'Bilirubine_indirecte', 'PAL_AMP' ,'PAL_DEA' ,'Diurèse', 'Protéines_ur',
                     'Microalbumine', 'Créatinine_ur' ,'Clairance' ,'Urée_ur' ,'Sodium_ur', 'Potasium_ur', 'Calcium_ur', 'Phosphore_ur',
                     'Acide_urique_ur', 'Glucose_ur', 'Amylase_ur']




class  EditBiochimieResultForm(forms.ModelForm):
      class Meta:
          model   = BiochimieResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service']

       # Resulta du biochime min

class BiochimieMinResultForm(forms.ModelForm):
      class Meta:
          model   = BiochimieMinResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service','medecin',
                      'Glucose' ,'Urée', 'Créatinine', 'NA','K', 'CA', 'ALB']


class  EditBiochimieMinResultForm(forms.ModelForm):
      class Meta:
          model   = BiochimieMinResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient',"Age"  , 'Service',
                      'Glucose' ,'Urée', 'Créatinine', 'NA','K', 'CA', 'ALB']
