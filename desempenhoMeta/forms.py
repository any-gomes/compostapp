from .models import Composteira
from django import forms
from desempenhoMeta.models import DesempenhoMeta

class DesempenhoMetaForms(forms.ModelForm):
    class Meta:
        model = desempenhoMeta
        fields = ('meta_concluido')

