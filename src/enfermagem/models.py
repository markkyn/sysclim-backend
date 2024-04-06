from datetime import datetime

from django.db import models

from common.models import ProfissionalSaude, Paciente

class Enfermeiro(models.Model):
    coren = models.CharField(
        unique = True,
        max_length = 12,
        primary_key = True,
    )

    profissional = models.ForeignKey(
        ProfissionalSaude,
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = 'enfermeiro'



class Vacina(models.Model):
    nome = models.CharField(
        max_length = 64,
        blank = False
    )

    lote = models.CharField(
        max_length = 24,
        null = False, 
        blank = False
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
        on_delete=models.DO_NOTHING
    )

    enfermeiro  = models.ForeignKey(
        Enfermeiro,
        null = True, # Caso não esteja aplicado = True
        blank = False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'vacina'
