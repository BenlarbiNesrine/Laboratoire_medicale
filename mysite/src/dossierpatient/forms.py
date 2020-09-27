from django import forms
from .models import DossierPatient


class DossierPatientForm(forms.ModelForm):
    class Meta:
        model   = DossierPatient
        fields  = ['Horodatage_création_de_dossier','nom_patient' , 'sexe' , 'date_de_naissance']

class EditDossierPatientForm(forms.ModelForm):
    class Meta:
        model   = DossierPatient
        fields  = ['nom_patient' , 'sexe' , 'date_de_naissance']
