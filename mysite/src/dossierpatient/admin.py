from django.contrib import admin
from .models import DossierPatient

# Register your models here.




class DossierPatientAdmin(admin.ModelAdmin):
    list_display = ["id" , "nom_patient" , "sexe","date_de_naissance","Horodatage_creation_de_dossier","email"]


admin.site.register(DossierPatient , DossierPatientAdmin)
