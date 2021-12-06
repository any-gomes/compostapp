from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

import acompanhamentoComposteira
from acompanhamentoComposteira.apps import AcompanhamentoComposteiraConfig
from meta.apps import MetaConfig
from insumo.models import Insumo


class Composteira(models.Model):
    nome = models.CharField(max_length=30)
    data_inicio_comp = models.DateField(auto_now_add=True, null=True, blank=True)
    tamanho_comp = models.IntegerField(null=True, blank=True)
    total_humus_produzido = models.FloatField(null=True, blank=True)
    concluido = models.BooleanField(null=True, blank=True)
    data_conclusao_comp = models.DateField(null=True, blank=True)
    qualidade = models.BooleanField(null=True, blank=True)
    insumo = models.ManyToManyField('insumo.Insumo', verbose_name="Lista de Insumos")
    humus_produzido = models.BooleanField(null=True, blank=True)
    meta = models.ManyToManyField('meta.MetaCompost', verbose_name="Lista de Metas")
    acompanhamento = models.ManyToManyField('acompanhamentoComposteira.AcompanhamentoComposteira', verbose_name="Lista de Acompanhamento")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'Composteira'

    # Métodos
    def __str__(self):
        return self.nome
        # return "{} ({})".format(self.data_inicio_comp, self.tamanho_comp)
    #def get_valorInsumo(self):
        #return self.insumo

    def calcula_score(self):
        max_tamanho = self.insumo.count()*3
        score = (sum(i.classificacao_insumo.pontuacao for i in self.insumo.all())/max_tamanho)*100
        return round(score,1)

    def adicionar_insumo(self):
        print("")

    def sugerir_insumo(self):
        print("")

    def calcular_qualidade_comp(self):
        print("")

    def calcular_temp_comp(self):
        print("")





