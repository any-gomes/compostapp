from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import composteira
import insumo

from .models import models
from composteira.models import Composteira
from insumo.forms import InsumoForms

# Create your views here.
def novoInsumo(request):
    if request.method == 'POST':
        nInsumo = InsumoForms(request.POST)

        if nInsumo.is_valid():
            insumo = nInsumo.save(commit=False)
            insumo = nInsumo.save()
            return redirect('/homeComposteira')
    else:
        nInsumo = InsumoForms()
        return render(request, 'account/addInsumo.html', {'form': nInsumo})