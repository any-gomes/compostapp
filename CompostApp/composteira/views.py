from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import composteira
import insumo

from .models import models
from composteira.models import Composteira
from composteira.forms import ComposteiraForms


# Create your views here.

"""def novoInsumo(request):
    nInsumo = insumo()
    return render(request,'account/addinsumo.html', {'insumo' : insumo})"""


def novaComposteira(request):
    if request.method == 'POST':
        nComposteira = ComposteiraForms(request.POST)

        if nComposteira.is_valid():
            cd = nComposteira.cleaned_data
            composteira = Composteira( nome=cd['nome'])
            composteira.save()

           # composteira = nComposteira.save()
            return redirect('/homeComposteira')
    else:
        nComposteira = ComposteiraForms()
        return render(request, 'account/addComposteira.html', {'form': nComposteira})

#def novaComposteira(request):
#    if request.method == 'POST':
#        nComposteira = ComposteiraForms(request.POST)

#        if nComposteira.is_valid():
#            composteira = nComposteira.save()
#            return redirect('/')

#    else:
#        nComposteira = ComposteiraForms()
#        return render(request, 'account/addComposteira.html', {'form': nComposteira})


def homeComposteira(request):
    return render(request, 'account/composteira.html')


def composteiraList(request):
    search = request.GET.get('search')
    if search:
        composteiras = Composteira.objects.filter(nome__icontains=search)
    
    else:
        composteiras = Composteira.objects.all().order_by('-data_inicio_comp')  # resgata objs do bd
    
    return render(request, 'account/composteira.html', {'composteiras': composteiras})  # envia para o template desejado


def composteiraView(request, id):
    composteiraV = get_object_or_404(Composteira, pk=id)
    return render(request, 'account/composteiraItem.html', {'composteira': composteiraV})


def editComposteiraM(request, id):
    composteiraE = get_object_or_404(Composteira, pk=id)

    if (request.method == 'POST'or None):
        #nome = request.POST.get('nome')
        form = ComposteiraForms(request.POST, instance=composteiraE)

        if (form.is_valid()):
            cd = form.cleaned_data
            composteiraE = Composteira( nome=cd['nome'] )
            composteiraE.save(commit=False)
            return redirect('/homeComposteira')
        else:
            return render(request, 'account/editComposteira.html', {'form': form, 'composteira': composteiraE})
    else:
        form = ComposteiraForms()
        return render(request, 'account/editComposteira.html', {'form': form, 'composteira': composteiraE})


def deleteComposteira(request, id):
    composteiraD = get_object_or_404(Composteira, pk=id)
    composteiraD.delete()

    messages.info(request, 'Composteira deletada com sucesso!')

    return redirect('/homeComposteira')


def novoInsumo(request):
    if request.method == 'POST':
        nInsumo = InsumoForms(request.POST)

        if nInsumo.is_valid():
            cd = nInsumo.cleaned_data
            insumo = Insumo( nome=cd['nome_insumo'])
            insumo.save()

           # composteira = nComposteira.save()
            return redirect('/')
    else:
        nInsumo = InsumoForms()
        return render(request, 'account/addinsumo.html', {'insumo': insumo})
        #return render(request, 'account/addinsumo.html', {'form': nInsumo})

def addDesempenhoMeta(request):
    if request.method == 'POST':
        nDesempenhoMeta = DesempenhoMetaForms(request.POST)

        if nDesempenhoMeta.is_valid():
            cd = nDesempenhoMeta.cleaned_data
            composteira = DesempenhoMetaForms(
                         nome=cd['meta_concluido']
                      )
            DesempenhoMeta.save()

           # composteira = nDesempenhoMeta.save()
            return redirect('/')


    else:
        nDesempenhoMeta = DesempenhoMeta()
        return render(request, 'account/addDesempenhoMeta.html', {'form': nDesempenhoMeta})
