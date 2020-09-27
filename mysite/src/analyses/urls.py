from django.conf.urls import url ,include
from . import views



urlpatterns = [


    url(r'Demande/Create-demande/$' , views.CreateDemandeDexam , name='CreateDemandeDexam'),
    url(r'Demande/Edit-demande/$' , views.EditDemandeDexam , name='EditDemandeDexam'),
    url(r'Demande/Delete-demande/$' , views.DeleteDemandeDexam , name='DeleteCreateDemandeDexam'),
    url(r'Result/Create-CoproParasitology-Result/$' , views.CreateCoproParasitologyResult , name='CreateCoproParasitologyResult'),
    url(r'Result/Edit-CoproParasitology-Result/$' , views.EditCoproParasitologyResult , name='EditCoproParasitologyResult'),
    url(r'Result/Create-Bilan-Urgence-Result/$' , views.CreateBilanDurgenceResult , name='CreateBilanDurgenceResult'),
    url(r'Result/Create-Biochimie-Result/$' , views.CreateBiochimieResult , name='CreateBiochimieResult'),
    url(r'Result/Create-Biochimie-min-Result/$' , views.CreateBiochimieMinResult , name='CreateBiochimieMinResult'),



]
