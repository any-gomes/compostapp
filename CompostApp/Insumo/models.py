from django.db import models

class Insumo(models.Model):
    nome_insumo = models.CharField(max_length = 20)
    data_inclusao = models.DateField(null = True, blank = True)
    qualidade = models.IntegerField(default=Classificacao.Bom, choices=Classificacao.choices)

# Metadados
class Meta:
        db_table = 'Insumo'

# Métodos

