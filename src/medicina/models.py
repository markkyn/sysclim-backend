from datetime import timedelta

from django.db import models
from django.db.models import Q

from common.models import *
from enfermagem.models import Vacina

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
   
    def verificar_disponibilidade(self, data_hora_inicio, duracao=1):
        data_hora_fim = data_hora_inicio + timedelta(hours=duracao)

        consultas_no_periodo = Consulta.objects.filter(
            Q(dh_realizacao__lt=data_hora_fim) &
            Q(dh_realizacao__gte=data_hora_inicio),
            medico=self
        ).exists()

        return not consultas_no_periodo
    
    def __str__(self):
        return f"{self.profissional.nome}({self.crm})"
    
    class Meta:
        db_table = 'medico'

class Consulta(models.Model):
    STATUS_CHOICES =(
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
        ('perdida', 'Perdida'),
    )



    dh_realizacao = models.DateTimeField(
        "Data e Hora de Realização",
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

    status = models.CharField(
        max_length=50,
        blank = False,
        null  = False,
        choices = STATUS_CHOICES,
        default = 'agendada'
    )

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING
    )

    def setNovoHorario(self, novo_horario):
        self.dh_realizacao = novo_horario

    class Meta:
        db_table = 'consulta'

class Exame(models.Model):
    tipo = models.CharField(
        max_length = 64,
    )
    
    dh_realizacao = models.DateTimeField(
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

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING
    )

    class Meta:
        db_table = 'exame'

class Prontuario(models.Model):
    dh_criacao = models.DateTimeField(
        default = datetime.now()
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.DO_NOTHING
    )

    def getAtestados(self):
        return Atestado.objects.filter(paciente=self.paciente)

    def getVacinasAplicadas(self):
        return Vacina.objects.filter(paciente=self.paciente)

    class Meta:
        db_table = 'prontuario'

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

    class Meta:
        db_table = 'atestado'