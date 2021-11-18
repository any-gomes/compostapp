from django.db import models

class Meta(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio_meta = models.DateField()
    data_fim_meta = models.DateField()
    concluida = models.BooleanField()
    desempenhoMeta = models.ForeignKey('DesempenhoMeta', on_delete=models.SET_NULL, null=True)

# Metadados
    class Meta:
        db_table = 'Meta'

# Métodos
    def adicionar_meta(self):
        print("")

    def excluir_meta(self):
        print("")

    def editar_meta(self):
        print("")

    def notificar_meta(self):
        print("")