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