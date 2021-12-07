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
    pontuacao_acomp = models.FloatField(null=True, blank=True, default=1)
    img_acomp = models.ImageField(null=True, upload_to='images/')

    # Metadados
    class Meta:
        db_table = 'AcompanhamentoComposteira'

    # Métodos
    def altera_pontuacao(self):
        if (self.moscas == True):
            self.pontuacao_acomp -= 0.1
        if (self.minhocas_morte == True):
            self.pontuacao_acomp -= 0.1
        if (self.muita_umidade == True):
            self.pontuacao_acomp -= 0.1
        if (self.odor_desagradavel == True):
            self.pontuacao_acomp -= 0.1
        

    def sugerir_melhoria(self):
        print("")

    # def __str__(self):
    # return self.acompanhamento_id

