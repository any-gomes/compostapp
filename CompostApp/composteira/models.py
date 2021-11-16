from django.db import models

class Composteira(models.Model):

   data_inicio_comp = models.DateField(null = True, blank = True)
   tamanho_comp =  models.IntegerField(null = True, blank = True)
   total_humus_produzido = models.FloatField(null = True, blank = True)
   concluido = models.BooleanField(null = True, blank = True)
   data_conclusao_comp = models.DateField(null = True, blank = True)
   qualidade = models.BooleanField(null = True, blank = True)
   insumo = models.ManyToManyField(Insumo, verbose_name="Lista de Insumos")
   humus_produzido = models.BooleanField(null = True, blank = True)
   meta = models.ManyToManyField(Meta, verbose_name="Lista de Meta")
   acompanhamento = models.ManyToManyField(Acompanhamento, verbose_name="Lista de Acompanhamento")

   class Meta:
        db_table = 'Composteira'

   # Métodos
   def __str__(self):
      return "{} ({})".format(self.data_inicio_comp, self.tamanho_comp)

   def acompanhar_comp(self):
      print("")
   def adicionar_insumo(self):
      print("")
   def sugerir_insumo(self):
      print("")
   def adicionar_comp(self):
      print("")
   def calcular_qualidade_comp(self):
      Print("")
   def calcular_temp_comp(self):
      Print("")



