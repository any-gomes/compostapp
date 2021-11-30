from .models import Composteira
from django import forms
from composteira.models import Composteira


class ComposteiraForms(forms.Form):
        model = Composteira
        nome = forms.CharField(max_length=30)

       # fields = '__all__'
       # fields = ('nome', 'tamanho_comp', 'humus_produzido')

