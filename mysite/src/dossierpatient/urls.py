from django.conf.urls import url ,include
from . import views




urlpatterns = [

    url(r'ListDossierPatient/$' , views.ListDossierPatient, name='DossierPatientList'),
    url(r'creation/$' , views.CreateDossierPatient , name='CreateDossierPatient'),
    url(r'edit/$' , views.EditDossierPatient , name='EditDossierPatient'),
    url(r'Organigramme/$' , views.DossierPatientOrganigramme.as_view() , name='DossierPatientOrganigramme'),
    #url(r'EditDossierPatient/$' , views.EditDossierPatient , name='EditDossierPatient'),
    url(r'exporter/svc/$' , views.exportcsv , name='exportcsv'),
    url(r'exporter/pdf/$' , views.exportpdf , name='exportpdf'),
    url(r'exporter/excel/$' , views.exportexcel , name='exportexcel'),



]
