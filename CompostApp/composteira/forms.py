from .models import Composteira
from django import forms
from composteira.models import Composteira


class ComposteiraForms(forms.Form):
        model = Composteira
        nome = forms.CharField(max_length=30)
        data_inicio_comp = forms.DateField(required=True)
        tamanho_comp = forms.IntegerField(required=True)
        data_conclusao_comp = forms.DateField(required=True)
        #insumo = forms.ManyToManyField(required=True)
       # fields = '__all__'
       # fields = ('nome', 'tamanho_comp', 'humus_produzido')

