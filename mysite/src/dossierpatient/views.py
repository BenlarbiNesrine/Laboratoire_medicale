from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DossierPatient
from .forms import DossierPatientForm
# Create your views here.




def CreateDossierPatient(request):
    if request.method == 'POST':
        form = DossierPatientForm(request.POST)
        if form.is_valid():
            new_form =form.save(commit = False)
            new_form.user = request.user
            new_form.save()




    else:
        form = DossierPatientForm()


    context = {
    'form' : form ,
    }

    return render (request , 'CreationDossierPatient.html' , context)
