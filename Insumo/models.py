from django.db import models

class Insumo(models.Model):
    nome_insumo = models.CharField(max_length = 20)
    qtd_insumo = models.IntegerField(null = True, blank = True)
    data_inclusao = models.DateField(null = True, blank = True)
    classificacao_insumo = models.IntegerField(default=Classificacao.Bom, choices=Classificacao.choices)
    retirado = models.BooleanField(null = True, blank = True)

# Metadados
class Meta:
        db_table = 'Insumo'

# Métodos

