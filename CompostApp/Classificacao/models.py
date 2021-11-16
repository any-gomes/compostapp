from django.db import models

class Classificacao(models.IntegerChoices):
    Bom = 3, 'Bom'
    Medio = -1, 'Medio'
    Ruim = -3, 'Ruim'

# Metadados
    class Meta:
        db_table = 'Classificacao'

# Métodos
    def pesquisar_pergunta(self):
        print("")

    def pesquisar_categoria(self):
        print("")