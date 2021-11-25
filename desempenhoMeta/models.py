from django.db import models

class DesempenhoMeta(models.Model):

    meta_concluido = models.IntegerField(default=0)

# Metadados
    class Meta:
        db_table = 'desempenhoMeta'

# Métodos
    def calcular_desempenho_meta(self):
        print("")