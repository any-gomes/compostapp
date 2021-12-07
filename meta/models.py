from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import IntegerField

class MetaCompost(models.Model):
    id_meta = IntegerField(models.UUIDField)
    nome = models.CharField(max_length=50)
    data_inicio_meta = models.DateField()
    data_fim_meta = models.DateField()
    concluida = models.BooleanField()
    desempenhoMeta = models.ForeignKey('desempenhoMeta.desempenhoMeta', on_delete=models.SET_NULL, null=True)

# Metadados
    class Meta:
        db_table = 'meta'

# Métodos
    def adicionar_meta(self):
        print("")

    def excluir_meta(self):
        print("")

    def editar_meta(self):
        print("")

    def notificar_meta(self):
        print("")