from django.db import models

class DesempenhoMeta(models.Model):
    meta_total = models.IntegerField(default=0)
    meta_concluido = models.IntegerField(default=0)
    meta_inicial = models.IntegerField(default=0)

# Metadados
    class Meta:
        db_table = 'DesempenhoMeta'

# Métodos
    def calcular_meta_total(self):
        print("")

    def adicionar_meta_concluido(self):
        print("")

    def adicionar_meta_a_iniciar(self):
        print("")

    def adicionar_meta_eficiente(self):
        print("")