from django.db import models

class Classificacao(models.Model):
    #Bom = 3
    #Medio = -1, 'Medio'
    #Ruim = -3, 'Ruim'
    nome_classificação = models.CharField(null=True, blank=True,max_length=10)
    pontuacao = models.IntegerField(null=True, blank=True)

# Metadados
    class Meta:
        db_table = 'classificacao'

# Métodos
    def __str__(self):
        return self.nome_classificação
   # def get_pontuacao(self):
       # return self.pontuacao