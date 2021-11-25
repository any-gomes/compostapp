from .models import Composteira
from django import forms
from insumo.models import Insumo

class InsumoForms(forms.ModelForm):
    class Meta:
        model = insumo
        fields = ('nome_insumo', 'qtd_insumo ', 'data_inclusao', 'retirado')

