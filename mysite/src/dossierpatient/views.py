from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from django.views.generic import ListView
from itertools import chain
from django.contrib import messages
from .models import DossierPatient
from .forms import DossierPatientForm
from .forms import EditDossierPatientForm
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.db.models import Sum
#from weasyprint import HTML
#import tempfile
import datetime
import csv
import xlwt


# Create your views here.

def exportcsv(request):
    response = HttpResponse(content_type=('text/csv'))
    response['Content-Disposition']='attachment; filename=ListDossierPatient'+ \
            str(datetime.datetime.now())+'.csv'
    writer   = csv.writer(response)
    writer.writerow(['Horodatage_creation_de_dossier','nom_patient' ,'date_de_naissance', 'sexe'])

    Dossiers = DossierPatient.objects.filter(user=request.user)

    for Dossier in Dossiers:
        writer.writerow([Dossier.Horodatage_creation_de_dossier, Dossier.nom_patient, Dossier.date_de_naissance, Dossier.sexe])

    return response


def exportexcel(request):
    response = HttpResponse(content_type=('application/ms-excel'))
    response['Content-Disposition']='attachment; filename=ListDossierPatient'+ \
            str(datetime.datetime.now())+'.xls'
    wb       = xlwt. Workbook(encoding='utf-8')
    ws       = wb.add_sheet('Dossiers')
    row_num  = 0
    font_style= xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Horodatage_creation_de_dossier','nom_patient' ,'date_de_naissance', 'sexe']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style= xlwt.XFStyle()
    rows = DossierPatient.objects.filter(user=request.user).values_list('Horodatage_creation_de_dossier','nom_patient' ,'date_de_naissance', 'sexe')

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response



def exportpdf(request):
    response = HttpResponse(content_type=('application/pdf'))
    response['Content-Disposition']='inline; attachment; filename=ListDossierPatient'+ \
             str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding']='binary'

    html_string=render_to_string('templates/pdf-output.html',{'templates':[],'total': 0})
    html =HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output=open(output.name, 'rb')
        response.write(output.read())
    return response



def ListDossierPatient(request):
  Dossier = DossierPatient.objects.all()
  acc_dict = {'main': Dossier}
  return render(request, 'DossierPatient_list.html', context=acc_dict)





def CreateDossierPatient(request):
    if request.method == 'POST':
        form = DossierPatientForm(request.POST)
        if form.is_valid():

            new_form =form.save(commit = False)
            new_form.user = request.user
            new_form.save()
            messages.success(request,"demande enregistrée")


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
