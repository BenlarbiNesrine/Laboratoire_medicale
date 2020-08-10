from django.conf.urls import url ,include
from . import views



urlpatterns = [


    url(r'Create/$' , views.CreateDossierPatient , name='CreateDossierPatient'),
    #url(r'EditDossierPatient/$' , views.EditDossierPatient , name='EditDossierPatient'),



]
