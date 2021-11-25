from django.db import models
from classificacao.models import Classificacao
class Insumo(models.Model):
    #insumo_id = models.AutoField(primary_key=True)
    nome_insumo = models.CharField(max_length = 20)
    qtd_insumo = models.IntegerField(null = True, blank = True)
    data_inclusao = models.DateField(null = True, blank = True)
    classificacao_insumo =  models.ForeignKey('classificacao.classificacao',on_delete=models.CASCADE, null= True, blank = True)
    retirado = models.BooleanField(null = True, blank = True)

# Metadados
class Meta:
        db_table = 'insumo'

# Métodos
def __str__(self):
    return self.nome_insumo