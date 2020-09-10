from django.conf.urls import url ,include
from . import views



urlpatterns = [


    url(r'Demande/Create-demande/$' , views.CreateDemandeDexam , name='CreateDemandeDexam'),
    url(r'Demande/Edit-demande/$' , views.EditDemandeDexam , name='EditDemandeDexam'),
    url(r'Demande/Delete-demande/$' , views.DeleteDemandeDexam , name='DeleteCreateDemandeDexam'),
    url(r'Demande/Result/Create-CoproParasitology-Result/$' , views.CreateCoproParasitologyResult , name='CreateCoproParasitologyResult'),
    url(r'Demande/Result/Edit-CoproParasitology-Result/$' , views.EditCoproParasitologyResult , name='EditCoproParasitologyResult'),




]
