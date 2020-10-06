from django import forms
from .models import ( DemandeDexamen , CoproParasitologyResult , BilanDurgenceResult , BiochimieResult , GroupageSanguin
                     , AcinetobacterResult , EnterocoqueResult , EnterobacteriesResult, StaphylocoqueResult, PseudomonasResult,
                     BacteriologieResult)



class DemandeDexamenForm(forms.ModelForm):
    class Meta:
        model   = DemandeDexamen
        fields  = ['Horodatage_création_de_demande' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_de_tube' ,"Nombre_de_tubes"   ,
                   'Nature_examen' , 'Symptomes' , 'Douleurs' , 'Diarrhée' ,
                   'Nausées' , 'Vomissement' , 'ballonnement_abdominal' , 'Constipation' ,'diabete', 'Fievre',
                   'Amaigrissement' , 'Autre', 'Examen_Complémentaire' ,'Diagnostic', ]

class EditDemandeDexamForm(forms.ModelForm):
    class Meta:
        model   = DemandeDexamen
        fields  = ['Horodatage_création_de_demande' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_de_tube' ,"Nombre_de_tubes"   ,
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
                   'Adresse' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' ,  'Autres','Cas_d_erreur']

        widgets={
          'Nom_patient': forms.TextInput(attrs={'class':'form-control-sm'}),
          'Adresse': forms.TextInput(attrs={'class':'form-control-sm'}),
          'Service': forms.Select(attrs={'class':'form-control form-control-sm'}),
          'Cas_d_erreur': forms.Select(attrs={'class':'form-control form-control-sm'}),
          'Age': forms.NumberInput(attrs={'class':'form-control-sm'}),
          'Horodatage_création_de_resultat': forms.DateTimeInput(attrs={'class':'form-control-sm'}),
        }

class EditCoproParasitologyResultForm(forms.ModelForm):
    class Meta:
        model   = CoproParasitologyResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service' ,
                   'Adresse' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' ,  'Autres', 'Cas_d_erreur']

  #Resultats du Bilan D'Urgence

class BilanDurgenceResultForm(forms.ModelForm):
    class Meta:
        model   = BilanDurgenceResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service','céphaline_kaolin','INR',
                   'prothrombine' ,'Glucose' , 'Urée', 'Créatinine', 'NA', 'K', 'Calcium_ionisé','CRP','Bilirubine_directe',
                    'Bilirubine_total', 'Cas_d_erreur','WBC','RBC','HGB','HCT','MCV','MCH','MCHC','PLT','LYM','NEUT','Troponine']

        widgets={
          'Nom_patient': forms.TextInput(attrs={'class':'form-control-sm'}),
          'Service': forms.Select(attrs={'class':'form-control form-control-sm'}),
          'Cas_d_erreur': forms.Select(attrs={'class':'form-control form-control-sm'}),
          'Age': forms.NumberInput(attrs={'class':'form-control-sm'}),
          'Horodatage_création_de_resultat': forms.DateTimeInput(attrs={'class':'form-control-sm'}),
        }

class  EditBilanDurgenceResultForm(forms.ModelForm):
    class Meta:
        model   = BilanDurgenceResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service', 'céphaline_kaolin', 'INR',
                   'prothrombine' , 'Glucose' , 'Urée', 'Créatinine', 'NA','K','Calcium_ionisé', 'CRP', 'Bilirubine_directe',
                   'Bilirubine_total' , 'Cas_d_erreur']

    #Resultats du Biochimie

#class BiochimieResultForm(forms.ModelForm):

#      class Meta:
#          model   = BiochimieResult
#          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service','praticien', 'Glucose' ,'Urée', 'Créatinine',
#                     'Acide_urique', 'Sodium', 'Potasium', 'Calcium_total', 'Calcium_ionisé', 'Phosphore', 'Magnésium', 'Fer',
#                     'Aspect_du_sérum', 'Cholestérol_total', 'Triglycérides', 'HDL_Cholestérol', 'LDL_Cholestérol', 'Protéines',
#                     'Albumine','Amylase', 'Lipase', 'CK_Homme' ,'CK_Femme','CK_MB', 'LDH' , 'GOT' , 'GPT', 'y_gt_h' ,'y_gt_f',
#                     'Bilirubine_total' , 'Bilirubine_directe' , 'Bilirubine_indirecte', 'PAL_AMP' ,'PAL_DEA' ,'Diurèse', 'Protéines_ur',
#                     'Microalbumine', 'Créatinine_ur' ,'Clairance' ,'Urée_ur' ,'Sodium_ur', 'Potasium_ur', 'Calcium_ur', 'Phosphore_ur',
#                     'Acide_urique_ur', 'Glucose_ur', 'Amylase_ur', 'Cas_d_erreur','Troponine', 'HBA1C','CRP']

class BiochimieResultForm(forms.ModelForm):

      class Meta:
          model   = BiochimieResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Service','praticien', 'Glucose' ,'Urée', 'Créatinine',
                     'Acide_urique', 'Sodium', 'Potasium', 'Calcium_total', 'Calcium_ionisé', 'Phosphore', 'Magnésium', 'Fer',
                     'Aspect_du_sérum', 'Cholestérol_total', 'Triglycérides', 'HDL_Cholestérol', 'LDL_Cholestérol', 'Protéines',
                     'Albumine','Amylase', 'Lipase', 'CK_Homme' ,'CK_Femme','CK_MB', 'LDH' , 'GOT' , 'GPT', 'y_gt_h' ,'y_gt_f',
                     'Bilirubine_total' , 'Bilirubine_directe' , 'Bilirubine_indirecte', 'PAL_AMP' ,'PAL_DEA' ,'Diurèse', 'Protéines_ur',
                     'Microalbumine', 'Créatinine_ur' ,'Clairance' ,'Urée_ur' ,'Sodium_ur', 'Potasium_ur', 'Calcium_ur', 'Phosphore_ur',
                     'Acide_urique_ur', 'Glucose_ur', 'Amylase_ur', 'Cas_d_erreur','Troponine', 'HBA1C','CRP']

          widgets={
            'Nom_patient': forms.TextInput(attrs={'class':'form-control-sm'}),
            'praticien': forms.TextInput(attrs={'class':'form-control-sm'}),
            'Service': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'Cas_d_erreur': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'Age': forms.NumberInput(attrs={'class':'form-control-sm'}),
            'Horodatage_création_de_resultat': forms.DateTimeInput(attrs={'class':'form-control-sm'}),
            'Aspect_du_sérum': forms.Select(attrs={'class':'form-control form-control-sm border-0'}),
          }

class  EditBiochimieResultForm(forms.ModelForm):
      class Meta:
          model   = BiochimieResult
          fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" ,  'Service','Cas_d_erreur']

      #groupage sanguin

class GroupageSanguinForm(forms.ModelForm):
    class Meta:
        model   = GroupageSanguin
        fields  = ['Horodatage_creation_de_groupage','Nom_patient' , 'Groupe' , 'Rh','Adresse']


class AcinetobacterResultForm(forms.ModelForm):
    class Meta:
        model   = AcinetobacterResult
        fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
                   'Référence', 'Age', 'Examen_Directe','Germe_isolé' , 'Observation']

        #EnterocoqueResult
class EnterocoqueResultForm(forms.ModelForm):
    class Meta:
        model   = EnterocoqueResult
        fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
                   'Référence', 'Age', 'Examen_Directe','Germe_isolé' , 'Observation']

        #EnterobacteriesResult
class EnterobacteriesResultForm(forms.ModelForm):
    class Meta:
        model   = EnterobacteriesResult
        fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
                   'Référence', 'Age', 'Examen_Directe','Germe_isolé' , 'Observation']

    #StaphylocoqueResult
class StaphylocoqueResultForm(forms.ModelForm):
   class Meta:
       model   = StaphylocoqueResult
       fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
                  'Référence', 'Age', 'Examen_Directe','Germe_isolé' , 'Observation']

    #PseudomonasResult
class PseudomonasResultForm(forms.ModelForm):
   class Meta:
       model   = PseudomonasResult
       fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
                  'Référence', 'Age', 'Examen_Directe','Germe_isolé' , 'Observation']

     #BacteriologieResult
class BacteriologieResultForm(forms.ModelForm):
  class Meta:
     model   = BacteriologieResult
     fields  = ['Horodatage_création_de_resultat','Nom_patient' , 'praticien' , 'Service','Nature_de_prelèvement',
              'Référence', 'Age', 'Cytologie', 'Culture']
