from django.contrib import admin
from .models import DemandeDexamen
#from .models import CoproParasitologyResult

# Register your models here.
class DemandeDexamenAdmin(admin.ModelAdmin):
    list_display = ["id" , 'Nom_patient' ,"Age" , 'Sexe' ,
                    'Service', 'Médecin_prescripteur' , 'Nature_de_prelèvement' , 'Nature_des_tubes' ,
                    "Nombre_de_tubes"  ,  'Nature_examen' ,'Diagnostic'     ]


admin.site.register(DemandeDexamen , DemandeDexamenAdmin)

#result section
   #copro-Parasitologie
