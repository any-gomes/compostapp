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
    msg_erro = models.CharField(default= "Erros encontrados! para resolvê-los faça as seguintes alterações:\n", max_length= 500)
    erro = models.BooleanField(default= False)
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
        return self.pontuacao_acomp
    def error_warning(self):
        if (self.moscas == True):
            self.erro = True
            self.msg_erro += "-Utilize de repelentes naturais como óleo de citronela e repelente de neem para afastar as moscas\n"
        if (self.minhocas_morte == True):
            self.erro = True
            self.msg_erro += "-Mova a composteira para um lugar ventilado e com sombra!\n"
        if (self.muita_umidade == True):
            self.erro = True
            self.msg_erro += "-adicione serragem e folhas secas para diminuir a umidade, mas cuidado para não adicionar serragem com produtos químicos\n"
        if (self.odor_desagradavel == True):
            self.erro = True
            self.msg_erro += "-Abra a tampa da composteira, remexa o conteúdo e adicione material seco, porém não coloque novos resíduos por pelo menos dois dias\n"
        return self.msg_erro

    def sugerir_melhoria(self):
        print("")

    # def __str__(self):
    # return self.acompanhamento_id

