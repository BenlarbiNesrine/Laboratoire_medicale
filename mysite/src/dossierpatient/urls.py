from django.conf.urls import url ,include

from . import views



urlpatterns = [

    url(r'dossierpatient/$' , views.DossierPatientList , name='DossierPatientList'),
    url(r'create/$' , views.CreateDossierPatient , name='CreateDossierPatient'),
    url(r'edit/$' , views.EditDossierPatient , name='EditDossierPatient'),
    #url(r'EditDossierPatient/$' , views.EditDossierPatient , name='EditDossierPatient'),



]
