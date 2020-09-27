from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DemandeDexamen
from .forms import DemandeDexamenForm
from .forms import EditDemandeDexamForm
from .forms import DemandeDexamenSearchForm
from .models import CoproParasitologyResult
from .forms import CoproParasitologyResultForm
from .forms import EditCoproParasitologyResultForm
from .models import BilanDurgenceResult
from .forms import BilanDurgenceResultForm
from .forms import EditBilanDurgenceResultForm
from .models import BiochimieResult
from .forms import BiochimieResultForm
from .forms import EditBiochimieResultForm
from .models import BiochimieMinResult
from .forms import BiochimieMinResultForm
from .forms import EditBiochimieMinResultForm



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


   #BiochimieMinResult

def CreateBiochimieMinResult(request):
    if request.method == 'POST':
        form = BiochimieMinResultForm(request.POST)
        if form.is_valid():
            new_form      = form.save(commit = False)
            new_form.user = request.user
            new_form.save()


    else:
        form = BiochimieMinResultForm()


    context = {
    'form' : form ,
    }

    return render (request , 'BiochimieMinResult.html' , context)


def EditBiochimieMinResult(request):
    if request.method == 'POST':
        form = EditBiochimieMinResultForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/analyses/Result')

    else:
        form = EditBiochimieMinResultForm( instance = request.user)
        args = {'form':form}
        return render (request , 'EditBiochimieMinResult.html' , args)
