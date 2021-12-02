from django import forms
from .models import Composteira

class ComposteiraForms(forms.ModelForm):
        class Meta:
                model = Composteira
                fields = ('nome', 'tamanho_comp', 'humus_produzido')

