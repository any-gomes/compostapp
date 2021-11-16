from django.db import models

class Ajuda(models.Model):
    pergunta = models.CharField(max_length = 100)
    resposta = models.CharField(max_length = 100)
    categoria = models.ForeignKey('CategoriaAjuda', on_delete=models.SET_NULL, null=True)

# Metadados
    class Meta:
        db_table = 'Ajuda'
