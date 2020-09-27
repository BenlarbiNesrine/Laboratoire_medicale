from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import DossierPatient
from .forms import DossierPatientForm
from .forms import EditDossierPatientForm
from django.views.generic import TemplateView
# Create your views here.


class DossierPatientList(ListView):
    template_name = 'DossierPatient_list.html'
    model = DossierPatient



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


def EditDossierPatient(request):
        if request.method == 'POST':
            form = EditDossierPatientForm(request.POST , instance = request.user)

            if form.is_valid() :
                form.save()
                return redirect('/dossierpatient')

        else:
            form = EditDossierPatientForm( instance = request.user)
            args = {'form':form}
            return render (request , 'EditDossierPatient.html' , args)






class DossierPatientOrganigramme(TemplateView):
    template_name ='chart/chart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = DossierPatient.objects.all()
        return context
