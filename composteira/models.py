from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import acompanhamentoComposteira
from acompanhamentoComposteira.apps import AcompanhamentoComposteiraConfig
from acompanhamentoComposteira.models import AcompanhamentoComposteira
from meta.apps import MetaConfig
import meta, insumo
from insumo.models import Insumo

class Composteira(models.Model):

   nome = models.CharField(max_length = 30)
   data_inicio_comp = models.DateField(auto_now_add=True, null = True, blank = True)
   tamanho_comp =  models.IntegerField(null = True, blank = True)
   total_humus_produzido = models.FloatField(null = True, blank = True)
   concluido = models.BooleanField(null = True, blank = True)
   data_conclusao_comp = models.DateField(null = True, blank = True)
   qualidade = models.FloatField(null = True, blank = True)
   insumo = models.ManyToManyField('insumo.Insumo', verbose_name="Lista de Insumos")
   humus_produzido = models.BooleanField(null = True, blank = True)
   #meta = models.ManyToManyField('Meta', verbose_name="Lista de Metas")
   acompanhamento = models.ForeignKey('acompanhamentoComposteira.AcompanhamentoComposteira',on_delete=models.CASCADE, null= True, blank = True)
   meta = models.ForeignKey('meta.Meta',on_delete=models.CASCADE, null= True, blank = True)
   
   # insumo = models.ForeignKey('insumo.Insumo', on_delete=models.CASCADE, )

   class Meta:
        db_table = 'Composteira'

   # Métodos
   def __str__(self):
      return self.nome
      #return "{} ({})".format(self.data_inicio_comp, self.tamanho_comp)
   def __init__(self, nome, tamanho):
      self.nome = nome
      self.data_inicio_comp = datetime.datetime.now() 
      self.insumo = []
      self.tamanho_comp = tamanho
      self.qualidade = 0
   def atualiza_acompanhamento(self, acompanhamento):
      self.acompanhamento = acompanhamento
   def adicionar_insumo(self, insumo):
      self.insumo.append(insumo)
   def remover_insumo(self, insumo):
      self.insumo.remove(insumo)
   def calcula_score(self):
      self.qualidade = 0
      for i in self.insumo:
         self.qualidade += i
      max_tamanho = (len(self.insumo) * 3) 
      self.qualidade = (self.qualidade / max_tamanho) * 100   
   def acompanhar_comp(self):
      print("")
   def adicionar_insumo(self):
        print("")
   def sugerir_insumo(self):
      print("")
   def calcular_qualidade_comp(self):
      print("")
   def calcular_temp_comp(self):
      print("")

created_at = models.CharField


