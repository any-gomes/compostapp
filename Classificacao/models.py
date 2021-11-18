from django.db import models

class Classificacao(models.IntegerChoices):
    Bom = 3, 'Bom'
    Medio = -1, 'Medio'
    Ruim = -3, 'Ruim'

    nome_classificação = models.CharField(max_length=10)
    pontuacao = models.IntegerField(null=True, blank=True)

# Metadados
    class Meta:
        db_table = 'Classificacao'

# Métodos
