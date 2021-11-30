from django.db import models


class AcompanhamentoComposteira(models.Model):
    # acompanhamento_id = models.IntegerField(primary_key=True)
    # composteira = models.ForeignKey('composteira.Composteira',on_delete=models.CASCADE,)
    data_acomp = models.DateField(null=True, blank=True)
    moscas = models.BooleanField(null=True, blank=True)
    minhocas_morte = models.BooleanField(null=True, blank=True)
    temperatura = models.FloatField(null=True, blank=True)
    muita_umidade = models.BooleanField(null=True, blank=True)
    odor_desagradavel = models.BooleanField(null=True, blank=True)
    pontuacao_acomp = models.IntegerField(null=True, blank=True)
    img_acomp = models.ImageField(null=True, upload_to='images/')

    # Metadados
    class Meta:
        db_table = 'AcompanhamentoComposteira'

    # Métodos
    def sugerir_melhoria(self):
        print("")

    def sugerir_melhoria(self):
        print("")

    # def __str__(self):
    # return self.acompanhamento_id

