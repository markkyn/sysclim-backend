from django.db import models
from django.db.models import Q
from django.apps import apps
from datetime import datetime

from autenticacao.models import *

# Uso Geral
class Endereco(models.Model):
    rua = models.CharField(
        max_length = 64,
        blank = False,
        null = False
    )
    bairro = models.CharField(
        max_length = 64,
        blank = False,
        null = False
    )
    
    numero = models.CharField(
        blank = False,
        null = True
    )

    complemento = models.CharField(
        blank = False,
        null = True,
    )

    estado = models.CharField(
        max_length = 2,
        blank = False,
        null = False,
    )
    
    cidade = models.CharField(
        max_length = 24,
        blank = False,
        null = False,

    )

    cep = models.CharField(
        max_length = 8,
        blank = False,
        null = True,

    )

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade} - {self.estado} - {self.cep}"

    class Meta:
        db_table = 'endereco'

# Profissionais
class Especialidade(models.Model):
    tuss = models.CharField( # código unico de especialidade de saúde
        max_length = 24,
        unique = True,
        primary_key = True
    )
    
    nome = models.CharField(
        max_length = 64,
        unique = True
    )

    def __str__(self) -> str:
        return f"{self.nome} ( TUSS: {self.tuss})"

    class Meta:
        db_table = 'especialidade'

class Sala(models.Model):
    numero = models.IntegerField(
        primary_key = True,
        null = False,
        blank = False
    )

    ativo = models.BooleanField(
        default=True,
        null = False
    )
    
    def verificar_disponibilidade(self, data_hora_inicio, duracao=1):
        Consulta = apps.get_model('common', 'Consulta')
        
        data_hora_fim = data_hora_inicio + datetime.timedelta(hours=duracao)

        consultas_no_periodo = Consulta.objects.filter(
            Q(dh_realizacao__lt=data_hora_fim) &
            Q(dh_realizacao__gte=data_hora_inicio),
            medico=self
        ).exists()

        return not consultas_no_periodo

    def __str__(self):
        return f"Sala {self.numero}"

    class Meta:
        db_table = 'sala'

class ProfissionalSaude(ModeloUsuario):
    cpf = models.CharField(
        primary_key = True,
        max_length = 11,
        unique = True,
    )

    nome = models.CharField(
        max_length = 64,
    )

    genero = models.CharField(
        max_length = 1,
    )
    
    dt_nascimento = models.DateField(
    )
    
    cargo = models.CharField(
    )

    ativo = models.BooleanField(
        default = True    
    )

    especialidade = models.ForeignKey(
        Especialidade,
        null = True,
        on_delete = models.SET_NULL
    )

    endereco = models.ForeignKey(
        Endereco,
        null = False,
        on_delete = models.CASCADE
    )

    @property
    def cpf_formatado(self):
        return f"{self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:11]}"

    def identificador_cargo(self):
        if self.cargo == "assistente":
            return Assistente.objects.get(profissional = self).id

    class Meta(ModeloUsuario.Meta):
        db_table = 'profissional'
    
# TODO: Incluir mais atributos relevantes para o Assistente ( talvez CPF e Formação )
class Assistente(models.Model):
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    nome = models.CharField(max_length = 64)


    def __str__(self):
        return self.email

    class Meta(ModeloUsuario.Meta):
        db_table = 'assistente'

class Escala(models.Model):
    dt_inicio = models.DateField()
    dt_final  = models.DateField()

    hr_inicio = models.TimeField()
    hr_final  = models.TimeField()

    ativo = models.BooleanField(
        default = True
    )

    class Meta:
        db_table = 'escala'

# Paciente
class Paciente(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    nome = models.CharField(
        max_length = 64,
        unique = True,
    )

    cpf = models.CharField(
        max_length = 11,
        unique = True,
        primary_key = True
    )
    
    genero = models.CharField(
        max_length = 1, 
        choices=GENERO_CHOICES
    )

    email = models.EmailField(
    )

    dt_nascimento = models.DateField(
        "Data de Nascimento",
        null  = False, 
        blank = False
    )

    endereco = models.ForeignKey(
        Endereco,
        on_delete = models.DO_NOTHING,
        default= None
    )

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING,
        default = None
    )

    def __str__(self):
        return f"{self.nome} ({self.cpf_formatado})"

    @property
    def cpf_formatado(self):
        return f"{self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:11]}"

    @property
    def getIdade(self):
        return datetime.now().year - self.dt_nascimento.year

    class Meta:
        db_table = 'paciente'