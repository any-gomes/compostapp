from django.db import models

class Notificacao(models.Model):
    data_notif = models.DateField(null = True, blank = True)
    titulo_notif = models.CharField(max_length = 20)
    descricao_notif = models.CharField(max_length = 200)
    usuario = models.ForeignKey('Usuario', on_delete = models.SET_NULL, null = True)
    meta = models.ForeignKey('Meta', on_delete = models.SET_NULL, null = True)

# Metadados
    class Meta:
        db_table = 'Notificacao'

# Métodos
    def enviar_notif(self):
        print("")

    def visualizar_notificacao(self):
        print("")
