from django.db import models

class Especialização(models.Model):
    nome = models.CharField(
        max_lenght = 64,
        required = True,
        unique = True
    )

class ProfissionalSaude(models.Model):
    nome = models.CharField(
        max_lenght = 64,
        required = True,
    )

    cpf = models.CharField(
        max_lenght = 11,
        required = True,
        unique = True
    )

class Medico(models.Model):
    crm = models.CharField(
        max_length = 12,
        primary_key = True,
        unique = True,
        required = True,

    )
    
    profissional = models.ForeignKey(
        ProfissionalSaude,
    )
    
class Enfermeiro(models.Model):
    coren = models.CharField(
        max_lenght = 12,
        primary_key = True,
        required = True,
        unique = True
    )

    profissional = models.ForeignKey(
        ProfissionalSaude,
    )


