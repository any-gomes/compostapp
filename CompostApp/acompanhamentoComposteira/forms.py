from django import forms
from .models import Composteira

class AcompanhamentoComposteiraForms(forms.ModelForm):
        class Meta:
                model = AcompanhamentoComposteira
                fields = ('moscas', 'minhocas_morte', 'temperatura', 'muita_umidade', 'odor_desagradavel')

