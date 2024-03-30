from django.db import models

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

class ProfissionalSaude(models.Model):
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
    
    email = models.EmailField(
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

# TODO: Incluir mais atributos relevantes para o Assistente ( talvez CPF e Formação )
class Assistente(models.Model):
    nome = models.CharField(
        max_length = 64,
    )

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
