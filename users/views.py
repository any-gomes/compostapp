from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

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
    form = ComposteiraForms(instance=Composteira) 
    
    if(request.method == 'POST'):
        form = ComposteiraForms(request.POST, instance=composteira)

        if(form.is_valid()):
            composteiraE.save()
            return redirect('/')
        else:
            return render(request, 'account/editComposteira.html', {'form' : form, 'composteira': composteiraE})
    else:
         return render(request, 'account/editComposteira.html', {'form' : form, 'composteira': composteiraE})  
