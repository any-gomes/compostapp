from .models import Composteira
from django import forms
from composteira.models import Composteira


class DesempenhoMetaForms(forms.Form):

        meta_concluido = models.IntegerField(default=0)

       # fields = ('nome', 'tamanho_comp', 'humus_produzido')

