from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DemandeDexamen
from .forms import DemandeDexamenForm
from .forms import EditDemandeDexamForm
from .models import CoproParasitologyResult
from .forms import CoproParasitologyResultForm
from .forms import EditCoproParasitologyResultForm

# Create your views here.
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
            return redirect('/analyses/Demande')

    else:
        form = EditCoproParasitologyResultForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditCoproParasitologyResult.html' , args)
