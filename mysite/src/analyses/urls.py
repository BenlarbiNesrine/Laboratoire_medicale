from django.conf.urls import url ,include
from . import views



urlpatterns = [


    url(r'Create-demande/$' , views.CreateDemandeDexam , name='CreateDemandeDexam'),
    #url(r'Create-Copro-Parasitology-Result/$' , views.CreateCoproParasitologyResult , name='CreateCoproParasitologyResult'),




]
