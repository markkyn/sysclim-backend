from django.db import models
from common.models import ProfissionalSaude


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
