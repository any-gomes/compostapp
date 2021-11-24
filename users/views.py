from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import composteira

from .models import models
from composteira.models import Composteira
from composteira.forms import ComposteiraForms
# Create your views here.

"""def novoInsumo(request):
    nInsumo = Insumo()
    return render(request,'account/addinsumo.html', {'insumo' : Insumo})"""

def novaComposteira(request):
    if request.method == 'POST':
        nComposteira = ComposteiraForms(request.POST)

        if nComposteira.is_valid():
            composteira = nComposteira.save()
            return redirect('/')

    else:
        nComposteira = ComposteiraForms()
        return render(request,'account/addComposteira.html', {'form' : nComposteira})
        
def homeComposteira(request):
        return render(request,'account/composteira.html')

def composteiraList(request):
    composteiras = Composteira.objects.all() #resgata objs do bd
    return render(request, 'account/composteira.html', {'composteiras': composteiras}) #envia para o template desejado

def composteiraView(request, id):
    composteiraV = get_object_or_404(Composteira, pk=id)
    return render(request, 'account/composteiraItem.html', {'composteira': composteiraV})

def editComposteiraM(request, id):
    composteiraE = get_object_or_404(Composteira, pk=id)
    form = ComposteiraForms(instance=composteiraE) 
    
    if(request.method == 'POST'):
        form = ComposteiraForms(request.POST, instance=composteiraE)

        if(form.is_valid()):
            composteiraE.save()
            return redirect('/homeComposteira')
        else:
            return render(request, 'account/editComposteira.html', {'form' : form, 'composteira': composteiraE})
    else:
         return render(request, 'account/editComposteira.html', {'form' : form, 'composteira': composteiraE})  


def deleteComposteira(request, id):
    composteiraD = get_object_or_404(Composteira, pk=id)
    composteiraD.delete()

    messages.info(request, 'Composteira deletada com sucesso!')


    return redirect('/homeComposteira')

