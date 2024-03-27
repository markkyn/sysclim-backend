from django.db import models
from common.models import ProfissionalSaude


class Medico(models.Model):
    crm = models.CharField(
        max_length = 12,
        primary_key = True,
        unique = True,
    )
    
    profissional = models.ForeignKey(
        ProfissionalSaude,
        on_delete = models.CASCADE
    )