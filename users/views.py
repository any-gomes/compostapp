from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import models
from insumo import Insumo
# Create your views here.

def novoInsumo(request):
    nInsumo = Insumo()
    return render(request,'account/addinsumo.html', {'insumo' : Insumo})

def novoInsumo(request):
    nInsumo = Insumo()
    return render(request,'account/addinsumo.html', {'insumo' : Insumo})