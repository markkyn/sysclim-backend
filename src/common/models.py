from django.db import models

# Uso Geral
class Endereco(models.Model):
    rua = models.CharField(
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
    )

# Profissionais
class Especializacao(models.Model):
    nome = models.CharField(
        max_length = 64,
        unique = True
    )
   
    tuss = models.CharField( # código unico de especialidade de saúde
        max_length = 24,
        unique = True,
        primary_key = True
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

class Assistente(models.Model):
    nome = models.CharField(
        max_length = 64,
    )