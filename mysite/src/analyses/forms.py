from django import forms
from .models import DemandeDexamen
#from .models import CoproParasitologyResult


class DemandeDexamenForm(forms.ModelForm):
    class Meta:
        model   = DemandeDexamen
        fields  = ['Nom_patient' ,"Age" , 'Sexe' , 'Service', 'Médecin_prescripteur' ,
                   'Nature_de_prelèvement' , 'Nature_des_tubes' ,"Nombre_de_tubes"   ,
                   'Nature_examen' ,'Diagnostic'  ]


#result section
   #CoproParasitologyResult

#class CoproParasitologyResultForm(forms.ModelForm):
#    class Meta:
#        model   = CoproParasitologyResult
    #    fields  = ['Nom_patient' ,"Age" , 'Sexe' , 'Service'  ]
