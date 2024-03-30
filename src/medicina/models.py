from datetime import datetime

from django.db import models

from common.models import *


class Medico(models.Model):
    crm = models.CharField(
        max_length = 12, 
        primary_key = True,
        unique = True,
    )
    
    profissional = models.ForeignKey(
        ProfissionalSaude,
        on_delete = models.CASCADE # TODO: não estou familiarizado com os tipos de on_delete (alterar ou manter)
    )

class Consulta(models.Model):
    dh_realizacao = models.DateTimeField(
        default = datetime.now()
    )

    objetivo = models.TextField(
        null = False,
        blank = True,
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.DO_NOTHING
    )

    medico = models.ForeignKey(
        Medico,
        on_delete = models.DO_NOTHING
    )

    sala = models.ForeignKey(
        Sala,
        on_delete = models.DO_NOTHING
    )

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING
    )

class Exame(models.Model):
    tipo = models.CharField(
        max_length = 64,
    )
    
    dh_realizacao = models.DateTimeField(
        default = datetime.now()
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.DO_NOTHING
    )

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING
    )

class Prontuario(models.Model):
    dh_criacao = models.DateTimeField(
        default = datetime.now()
    )

    medico = models.ForeignKey(
        Medico,
        on_delete = models.DO_NOTHING
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.DO_NOTHING
    )


class Atestado(models.Model):
    dh_criacao = models.DateTimeField(
        default = datetime.now()
    )

    informacoes = models.TextField()

    medico = models.ForeignKey(
        Medico,
        on_delete = models.DO_NOTHING
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.DO_NOTHING
    )
