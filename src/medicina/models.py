from django.db import models
from common.models import ProfissionalSaude


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