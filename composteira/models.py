from django.contrib.auth.models import AbstractUser
from django.db import models

import acompanhamentoComposteira
from acompanhamentoComposteira.apps import AcompanhamentoComposteiraConfig
from meta.apps import MetaConfig
import meta, insumo

class Composteira(models.Model):

   nome = models.CharField(max_length = 30)
   data_inicio_comp = models.DateField(null = True, blank = True)
   tamanho_comp =  models.IntegerField(null = True, blank = True)
   total_humus_produzido = models.FloatField(null = True, blank = True)
   concluido = models.BooleanField(null = True, blank = True)
   data_conclusao_comp = models.DateField(null = True, blank = True)
   qualidade = models.BooleanField(null = True, blank = True)
   #insumo = models.ManyToManyField(Insumo, verbose_name="Lista de Insumos")
   humus_produzido = models.BooleanField(null = True, blank = True)
   #meta = models.ManyToManyField(MetaConfig)
   acompanhamento = models.ForeignKey('AcompanhamentoComposteira',on_delete=models.CASCADE,)
   #meta = models.ForeignKey(meta,on_delete=models.CASCADE,)
   insumo = models.ForeignKey('Insumo', on_delete=models.CASCADE, )

   class Meta:
        db_table = 'Composteira'

   # Métodos
   def __str__(self):
      return "{} ({})".format(self.data_inicio_comp, self.tamanho_comp)

   def adicionar_meta(self):
      print("")
   def adicionar_acomp(self):
      print("")
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


