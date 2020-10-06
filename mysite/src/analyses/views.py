from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from .models import ( DemandeDexamen, CoproParasitologyResult, BilanDurgenceResult, BiochimieResult, GroupageSanguin, AcinetobacterResult,
                     EnterocoqueResult, EnterobacteriesResult, StaphylocoqueResult, PseudomonasResult, BacteriologieResult )
from .forms import ( DemandeDexamenForm, DemandeDexamenSearchForm, CoproParasitologyResultForm, BilanDurgenceResultForm, BiochimieResultForm,
                     GroupageSanguinForm, AcinetobacterResultForm, EnterocoqueResultForm, EnterobacteriesResultForm, StaphylocoqueResultForm,
                     PseudomonasResultForm, BacteriologieResultForm)
from .forms import EditDemandeDexamForm
from .forms import EditCoproParasitologyResultForm
from .forms import EditBilanDurgenceResultForm
from .forms import EditBiochimieResultForm
from django.template.loader import render_to_string
from django.db.models import Sum
#from weasyprint import HTML
#import tempfile
import datetime
import csv
import xlwt


# Create your views here.
    #exporter groupage sanguin

def exportcsv(request):
    response = HttpResponse(content_type=('text/csv'))
    response['Content-Disposition']='attachment; filename=ListeGroupageSanguin'+ \
            str(datetime.datetime.now())+'.csv'
    writer   = csv.writer(response)
    writer.writerow(['Horodatage_creation_de_groupage','Nom_patient' ,'Groupe', 'Rh'])

    groupe =  GroupageSanguin.objects.filter(user=request.user)

    for groupes in groupe:
        writer.writerow([groupes.Horodatage_creation_de_groupage, groupes.Nom_patient, groupes.Groupe, groupes.Rh])

    return response


def exportexcel(request):
    response = HttpResponse(content_type=('application/ms-excel'))
    response['Content-Disposition']='attachment; filename=ListeGroupageSanguin'+ \
            str(datetime.datetime.now())+'.xls'
    wb       = xlwt. Workbook(encoding='utf-8')
    ws       = wb.add_sheet('analyses')
    row_num  = 0
    font_style= xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Horodatage_creation_de_groupage','Nom_patient' ,'Groupe', 'Rh']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style= xlwt.XFStyle()
    rows = GroupageSanguin.objects.filter(user=request.user).values_list('Horodatage_creation_de_groupage','Nom_patient' ,'Groupe', 'Rh')

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response



def exportpdf(request):
    response = HttpResponse(content_type=('application/pdf'))
    response['Content-Disposition']='inline; attachment; filename=ListeGroupageSanguin'+ \
             str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding']='binary'

    html_string=render_to_string('templates/ListeGroupageSanguin-pdf-output.html',{'templates':[],'total': 0})
    html =HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output=open(output.name, 'rb')
        response.write(output.read())
    return response


         # create demande d examen de prélèvement

def CreateDemandeDexam(request):
    if request.method == 'POST':
        form = DemandeDexamenForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = DemandeDexamenForm()


    context = {
    'form' : form ,
    }

    return render (request , 'CreateDemandeDexam.html' , context)


def EditDemandeDexam(request):
    if request.method == 'POST':
        form = EditDemandeDexamForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/analyses/Demande')

    else:
        form = EditDemandeDexamForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditDemandeDexam.html' , args)


def DeleteDemandeDexam(request, id):
    template = 'CreateDemandeDexam.html'
    post     = get_object_or_404(Post, id=id)
    try:
        if request.methode =='POST':
           form = DeleteDemandeDexamForm(request.POST, instance=DemandeDexamen)
           post.delete()
           message.success(request, 'La demande est supprimée')
        else:
            form = DeleteDemandeDexamForm(instance=DemandeDexamen)
    except Exception as e:
        messages.warning(request,'La demande ne peut pas etre supprimée' )
    context = {'form': form , 'post': DemandeDexamen}




# result section
              #examen copro-parasitologie

def CreateCoproParasitologyResult(request):
    if request.method == 'POST':
        form = CoproParasitologyResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = CoproParasitologyResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'CoproParasitologyResult.html' , context)


def EditCoproParasitologyResult(request):
    if request.method == 'POST':
        form = EditCoproParasitologyResultForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/analyses/Result')

    else:
        form = EditCoproParasitologyResultForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditCoproParasitologyResult.html' , args)




        # Resultats du bilan d'urgence

def CreateBilanDurgenceResult(request):
    if request.method == 'POST':
        form = BilanDurgenceResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = BilanDurgenceResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'BilanDurgenceResult.html' , context)


def EditBilanDurgenceResult(request):
    if request.method == 'POST':
        form = EditBilanDurgenceResultForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/analyses/Result')

    else:
        form = EditBilanDurgenceResultForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditBilanDurgenceResult.html' , args)




       #BiochimieResult

def CreateBiochimieResult(request):
    if request.method == 'POST':
        form = BiochimieResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = BiochimieResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'BiochimieResult.html' , context)


def EditBiochimieResult(request):
    if request.method == 'POST':
        form = EditBiochimieResultForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/analyses/Result')

    else:
        form = EditBiochimieResultForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditBiochimieResult.html' , args)

     #groupage sanguin

def  ListeGroupageSanguin(request):
  groupe =  GroupageSanguin.objects.all()
  acc_dict = {'main': groupe}
  return render(request, 'listeGroupageSaunguin.html', context=acc_dict)

def CreateGroupageSanguin(request):
    if request.method == 'POST':
        form = GroupageSanguinForm(request.POST)
        if form.is_valid():

            new_form =form.save(commit = False)
            new_form.user = request.user
            new_form.save()



    else:
        form = GroupageSanguinForm()

    context = {
    'form' : form ,
    }

    return render (request , 'CreationGroupageSanguin.html' , context)

   #Microbiologie
   #CreateAcinetobacterResult

def CreateAcinetobacterResult(request):
    if request.method == 'POST':
        form = CreateAcinetobacterResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = AcinetobacterResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'Bact-Anti-Acinetobacter.html' , context)

                  #EnterocoqueResult

def CreateEnterocoqueResult(request):
    if request.method == 'POST':
        form = EnterocoqueResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = EnterocoqueResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'Bact-Anti-Entrerocoque.html' , context)

         #EnterobacteriesResult
def CreateEnterobacteriesResult(request):
    if request.method == 'POST':
        form = EnterobacteriesResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = EnterobacteriesResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'Bact-Anti-Enterobacteries.html' , context)


     #StaphylocoqueResult

def CreateStaphylocoqueResult(request):
    if request.method == 'POST':
        form = StaphylocoqueResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = StaphylocoqueResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'Bact-Anti-Staphylocoque.html' , context)


     #PseudomonasResult

def CreatePseudomonasResult(request):
   if request.method == 'POST':
      form = PseudomonasResultForm(request.POST)
      if form.is_valid():
          new_form      = form.save(commit = False)
          new_form.user = request.user
          new_form.save()


   else:
      form = PseudomonasResultForm()


   context = {
   'form' : form ,
   }

   return render (request , 'Bact-Anti-Psudomonas.html' , context)

    #BacteriologieResult

def CreateBacteriologieResult(request):
   if request.method == 'POST':
      form = BacteriologieResultForm(request.POST)
      if form.is_valid():
          new_form      = form.save(commit = False)
          new_form.user = request.user
          new_form.save()


   else:
      form = BacteriologieResultForm()


   context = {
   'form' : form ,
   }

   return render (request , 'Bact-Anti-ResultatBacteriologie.html' , context)
