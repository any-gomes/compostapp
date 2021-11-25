from django.db import models

class AcompanhamentoComposteira(models.Model):
    #acompanhamento_id = models.IntegerField(primary_key=True)
    #composteira = models.ForeignKey('composteira.Composteira',on_delete=models.CASCADE,)
    data_acomp = models.DateField(null = True, blank = True)
    moscas = models.BooleanField(null = True, blank = True)
    minhocas_morte = models.BooleanField(null=True, blank=True)
    temperatura = models.FloatField(null = True, blank = True)
    muita_umidade = models.BooleanField(null = True, blank = True)
    odor_desagradavel = models.BooleanField(null=True, blank=True)
    pontuacao_acomp = models.IntegerField(null = True, blank = True)
    img_acomp = models.ImageField(null = True, upload_to='images/')
    msg_error = models.CharField(null = True)

    # Metadados
    class Meta:
        db_table = 'AcompanhamentoComposteira'

    # Métodos
    def sugerir_melhoria (self):
      print("")

    def sugerir_melhoria (self):
      print("")
    def __init__(self, moscas, minhocas, umidade, odor):
      self.moscas = moscas
      self.minhocas_morte = minhocas
      self.muita_umidade = umidade
      self.odor_desagradavel = odor
      self.msg_error = "Para resolver os erros é recomendado fazer:\n"
    def __init__(self, moscas, minhocas, umidade, odor, temperatura):
      self.moscas = moscas
      self.minhocas_morte = minhocas
      self.muita_umidade = umidade
      self.odor_desagradavel = odor
      self.temperatura = temperatura
      self.msg_error = "Para resolver os erros é recomendado fazer:\n"
    def calcula_pontuacao(self):
      self.pontuacao_acomp = 0
      contador = 0
      if self.minhocas_morte == True:
        self.msg_error += "Minhocas morrendo deve-se fazer x\n"
        self.pontuacao_acomp += 3
        contador += 1
      if self.moscas == True:
        self.msg_error += "Moscas deve-se aumnentar a temperatura\n"
        self.pontuacao_acomp += 3
        contador += 1
      if self.muita_umidade == True:
        self.msg_error += "Umidade alta deve fazer y\n"
        self.pontuacao_acomp += 3
        contador += 1
      if self.odor_desagradavel == True:
        self.msg_error += "Fedor deve-se fazer z\n"
        self.pontuacao_acomp += 3
        contador += 1
    #def __str__(self):
      #return self.acompanhamento_id

    