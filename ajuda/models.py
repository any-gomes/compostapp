from django.db import models

class CategoriaAjuda(models.Model):

    categoria = models.ForeignKey('CategoriaAjuda', on_delete=models.SET_NULL, null=True)

# Metadados
    class Meta:
        db_table = 'CategoriaAjuda'
