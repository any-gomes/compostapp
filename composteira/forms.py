from .models import Composteira
from django import forms
from composteira.models import Composteira

class ComposteiraForms(forms.ModelForm):
    class Meta:
        model = Composteira
        fields = ('nome', 'tamanho_comp')

