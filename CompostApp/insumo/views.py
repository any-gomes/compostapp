from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

import insumo


from insumo.models import Insumo
from insumo.forms import InsumoForms


def Cascadingdllitems(request):
    Insumoobj = Insumo.objects.all()
    return render(request, 'account/addinsumo.html',{"Insumodata": Insumoobj})

def novoInsumo(request):
    if request.method == 'POST':
        nInsumo = InsumoForms(request.POST)

        if nInsumo.is_valid():
            insumo = nInsumo.save()
            return redirect('/homeComposteira')
    else:
        nInsumo = InsumoForms()
        return render(request, 'account/addinsumo.html', {'form': nInsumo})

def insumoList(request):
    insumos = Insumo.objects.all()
    return render(request, 'account/addinsumo.html', {'insumos': insumos})  # envia para o template desejado