from .models import Composteira
from django import forms
from composteira.models import Composteira

class ComposteiraForms(forms.ModelForm):
        model = Composteira
        fields = ('nome', 'tamanho_comp', 'humus_produzido')

