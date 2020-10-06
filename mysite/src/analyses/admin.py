from django.contrib import admin
from .models import ( DemandeDexamen, BilanDurgenceResult, CoproParasitologyResult, BiochimieResult, GroupageSanguin,AcinetobacterResult,
                      EnterocoqueResult, EnterobacteriesResult, StaphylocoqueResult, PseudomonasResult, BacteriologieResult)


# Register your models here.

class DemandeDexamenAdmin(admin.ModelAdmin):
    list_display = ["id" , 'Nom_patient' ,"Age" , 'Sexe' ,
                    'Service', 'Médecin_prescripteur' , 'Nature_de_prelèvement' , 'Nature_de_tube' ,
                    "Nombre_de_tubes"  ,  'Nature_examen' ,'Diagnostic'  ,'Horodatage_création_de_demande'   ]


admin.site.register(DemandeDexamen , DemandeDexamenAdmin)

#result section
   #copro-Parasitologie

class CoproParasitologyResultAdmin(admin.ModelAdmin):
    list_display = ["id" , 'Nom_patient' ,"Age" ,
                    'Service' , 'Horodatage_création_de_resultat' ]


admin.site.register(CoproParasitologyResult , CoproParasitologyResultAdmin)

   #bilan d'urgence

class BilanDurgenceResultAdmin(admin.ModelAdmin):
    list_display = ["id" , 'Nom_patient' ,"Age" ,
                    'Service' , 'Horodatage_création_de_resultat' ]


admin.site.register(BilanDurgenceResult , BilanDurgenceResultAdmin)

     #biochimie

class BiochimieResultAdmin(admin.ModelAdmin):
 list_display = ["id" , 'Nom_patient' ,"Age" ,
                 'Service' , 'Horodatage_création_de_resultat' ]


admin.site.register(BiochimieResult , BiochimieResultAdmin)

    #groupage sanguin
class GroupageSanguinAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Groupe", "Rh", "Horodatage_creation_de_groupage"]


admin.site.register(GroupageSanguin , GroupageSanguinAdmin)

           #AcinetobacterResult----------bactério-------------------
class AcinetobacterResultAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(AcinetobacterResult , AcinetobacterResultAdmin)

         #EnterocoqueResult
class EnterocoqueResultAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(EnterocoqueResult , EnterocoqueResultAdmin)

      #EnterobacteriesResult
class EnterobacteriesResultAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(EnterobacteriesResult , EnterobacteriesResultAdmin)

                      #StaphylocoqueResult
class StaphylocoqueResultAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(StaphylocoqueResult , StaphylocoqueResultAdmin)

              #PseudomonasResult
class PseudomonasResultAdmin(admin.ModelAdmin):
     list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(PseudomonasResult ,PseudomonasResultAdmin)

                #BacteriologieResult
class BacteriologieResultAdmin(admin.ModelAdmin):
    list_display = ["id" , "Nom_patient" , "Horodatage_création_de_resultat"]


admin.site.register(BacteriologieResult ,BacteriologieResultAdmin)
