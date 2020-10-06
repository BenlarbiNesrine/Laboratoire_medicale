from django.conf.urls import url ,include
from . import views



urlpatterns = [


    url(r'Demande/Creation/$' , views.CreateDemandeDexam , name='CreateDemandeDexam'),
    url(r'Demande/Modification/$' , views.EditDemandeDexam , name='EditDemandeDexam'),
    url(r'Demande/Suppression/$' , views.DeleteDemandeDexam , name='DeleteCreateDemandeDexam'),
    url(r'Result/CoproParasitology/Creation/$' , views.CreateCoproParasitologyResult , name='CreateCoproParasitologyResult'),
    url(r'Result/CoproParasitology/Modification$' , views.EditCoproParasitologyResult , name='EditCoproParasitologyResult'),
    url(r'Result/Bilan-Urgence-Result/Creation/$' , views.CreateBilanDurgenceResult , name='CreateBilanDurgenceResult'),
    url(r'Result/Biochimie/Creation/$' , views.CreateBiochimieResult , name='CreateBiochimieResult'),
    url(r'Result/Microbiologie/AcinetobacterResult/Creation/$' , views.CreateAcinetobacterResult, name='CreateAcinetobacterResult'),
    url(r'Result/Microbiologie/Enterocoque/Creation/$' , views.CreateEnterocoqueResult, name='CreateEnterocoqueResult'),
    url(r'Result/Microbiologie/Enterobacteries/Creation/$' , views.CreateEnterobacteriesResult, name='CreateEnterobacteriesResult'),
    url(r'Result/Microbiologie/Staphylocoque/Creation/$' , views.CreateStaphylocoqueResult, name='CreateStaphylocoqueResult'),
    url(r'Result/Microbiologie/Pseudomonas/Creation/$' , views.CreatePseudomonasResult, name='CreatePseudomonasResult'),
    url(r'Result/Microbiologie/Resultat-Bactériologie/Creation/$' , views.CreateBacteriologieResult, name='CreateBacteriologieResult'),
    url(r'Result/hemobiologie/Groupage-Sanguin/Liste/$' , views.ListeGroupageSanguin, name='ListeGroupageSanguin'),
    url(r'Result/hemobiologie/Groupage-Sanguin/Creation/$' , views.CreateGroupageSanguin, name='CreateGroupageSanguin'),
    url(r'Result/hemobiologie/Groupage-Sanguin/Liste/exporter/svc/$' , views.exportcsv , name='exportcsv'),
    url(r'Result/hemobiologie/Groupage-Sanguin/Liste/exporter/pdf/$' , views.exportpdf , name='exportpdf'),
    url(r'Result/hemobiologie/Groupage-Sanguin/Liste/exporter/excel/$' , views.exportexcel , name='exportexcel'),

]
