from django.db import models

TIPO = (
    'MINI', 'GESTAO'
)
class Orcamento(models.Model):
    cliente = models.TextField(max_length=30)
    tipo_hiper = models.TextField(choices=TIPO, max_length=30)
    boleto = models.BooleanField()
    nfse = models.BooleanField()
    spedc = models.BooleanField()