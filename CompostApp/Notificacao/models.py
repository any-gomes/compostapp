from django.db import models

class Notificacao(models.Model):
    data_not = models.DateField(null = True, blank = True)
    title = models.CharField(max_length = 20)
    desc_not = models.CharField(max_length = 200)
    meta = models.ForeignKey('Meta', on_delete = models.SET_NULL, null = True)

# Metadados
    class Meta:
        db_table = 'Notificacao'

# Métodos
    def enviar_notif(self):
        print("")

    def visualizar_notificacao(self):
        print("")
