from django.conf.urls import url ,include
from . import views
from .views import DossierPatientList



urlpatterns = [

    url(r'ListDossierPatient/$' , DossierPatientList.as_view() , name='DossierPatientList'),
    url(r'create/$' , views.CreateDossierPatient , name='CreateDossierPatient'),
    url(r'edit/$' , views.EditDossierPatient , name='EditDossierPatient'),
    url(r'Organigramme/$' , views.DossierPatientOrganigramme.as_view() , name='DossierPatientOrganigramme'),
    #url(r'EditDossierPatient/$' , views.EditDossierPatient , name='EditDossierPatient'),



]
