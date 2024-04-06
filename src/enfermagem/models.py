from datetime import datetime, date

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

    def __str__(self) -> str:
        return f"{self.profissional.nome} - COREN: {self.coren}"


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

    dt_fabricacao = models.DateField(
        null = False
    )

    dt_validade = models.DateField(
        null = False
    )

    dh_aplicacao = models.DateTimeField(
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

    def filtrarAplicaveis():
        return Vacina.objects.filter(
            paciente = None, 
            dt_validade__gte = datetime.now()
        )

    @property
    def status(self):
        if self.dt_validade < date.today() and not self.paciente:
            return "Vencida"

        return "Aplicada" if self.paciente else "Não aplicada"

    def __str__(self):
        return f"{self.nome} - {self.lote}"

    class Meta:
        db_table = 'vacina'
