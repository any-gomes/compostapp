from .models import Composteira
from django import forms
from insumo.models import Insumo

class InsumoForms(forms.ModelForm):
    class Meta:
        model = Insumo
        nome_insumo = forms.CharField(max_length = 20, required = True)
        qtd_insumo = forms.IntegerField(required = True)
        data_inclusao = forms.DateField(required = True)

        fields = ('nome_insumo', 'qtd_insumo ', 'data_inclusao', 'retirado')
