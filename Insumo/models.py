from django.db import models
import classificacao
class Insumo(models.Model):
    insumo_id = models.IntegerField(primary_key=True)
    nome_insumo = models.CharField(max_length = 20)
    qtd_insumo = models.IntegerField(null = True, blank = True)
    data_inclusao = models.DateField(null = True, blank = True)
    #classificacao_insumo = models.IntegerField(default=classificacao.Bom, choices=classificacao.choices)
    retirado = models.BooleanField(null = True, blank = True)

# Metadados
class Meta:
        db_table = 'Insumo'

# Métodos
def __str__(self):
    return self.insumo_id
