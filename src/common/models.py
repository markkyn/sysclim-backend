from django.db import models

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

class Sala(models.Model):
    numero = models.IntegerField(
        primary_key = True,
        null = False,
        blank = False
    )

    especialidade = models.ForeignKey(
        Especialidade,
        null = True,
        on_delete = models.SET_NULL
    )

    disponivel = models.BooleanField(
        default = True,
    )

class Assistente(models.Model):
    nome = models.CharField(max_length = 64)

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

# Paciente
class Paciente(models.Model):
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
    )

    email = models.EmailField(
    )

    dt_nascimento = models.DateField(
        null  = False, 
        blank = False
    )

    created_by = models.ForeignKey(
        Assistente,
        on_delete = models.DO_NOTHING,
        default = None
    )
