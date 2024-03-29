from django.shortcuts import render

from datetime import datetime

from common.models import *

class Vacina(models.Model):
    nome = models.CharField(
        max_length = 64,
        blank = False
    )

    lote = models.CharField(
        max_length = 24,
        null = False, 
        blanck = False
    )

    dt_cadastro = models.DateTimeField(
        default = datetime.now(),
        null = True
    )

    descricao = models.TextField()

    paciente = models.ForeignKey(
        Paciente,
        null = True, # Caso não esteja aplicado = True
        blank = False,
    )

    enfermeiro  = models.ForeignKey(
        Enfermeiro,
        null = True, # Caso não esteja aplicado = True
        blank = False,
    )

