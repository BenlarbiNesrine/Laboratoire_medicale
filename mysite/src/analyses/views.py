from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DemandeDexamen
from .forms import DemandeDexamenForm
#from .models import CoproParasitologyResult
#from .forms import CoproParasitologyResultForm

# Create your views here.

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




# result section
              #examen copro-parasitologie

#def CreateCoproParasitologyResult(request)
