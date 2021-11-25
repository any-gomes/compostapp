from .models import Composteira
from django import forms
from meta.models import Meta

class MetaForms(forms.ModelForm):
    class Meta:
        model = meta
        fields = ('nome', 'data_inicio_meta ', 'data_fim_meta', 'concluida')

