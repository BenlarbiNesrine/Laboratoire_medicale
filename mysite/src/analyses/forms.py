from django import forms
from .models import DemandeDexamen
from .models import CoproParasitologyResult


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
#result section
   #CoproParasitologyResult

class CoproParasitologyResultForm(forms.ModelForm):
    class Meta:
        model   = CoproParasitologyResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service' ,
                   'Adresse' , 'Symptomes' , 'Douleurs' , 'Diarrhée' , 'Examen_Complémentaire' ,
                   'Nausées' , 'Vomissement' , 'ballonnement_abdominal' , 'Constipation' ,
                   'Amaigrissement' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' , 'Autre']

class EditCoproParasitologyResultForm(forms.ModelForm):
    class Meta:
        model   = CoproParasitologyResult
        fields  = ['Horodatage_création_de_resultat' , 'Nom_patient' ,"Age" , 'Sexe' , 'Service' ,
                   'Adresse' , 'Symptomes' , 'Douleurs' , 'Diarrhée' , 'Examen_Complémentaire' ,
                   'Nausées' , 'Vomissement' , 'ballonnement_abdominal' , 'Constipation' ,
                   'Amaigrissement' ,  'Résultat' , 'Macroscopie' , 'Microscopie' , 'Etat_frais' ,
                   'Ritchie' , 'Kato_Willis' , 'Scotch_test' , 'Autre']
