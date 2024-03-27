from django.db import models

# Uso Geral
class Endereco(models.Model):
    rua = models.CharField(
        max_lenght = 64,
        required = True
    )
    
    numero = models.CharField(
        required = False
    )

    complemento = models.CharField(
        required = False,
    )

    estado = models.CharField(
        max_lenght = 2
    )
    
    cidade = models.CharField(
        max_lenght = 24
    )

    cep = models.CharField(
        max_lenght = 8
    )

# Paciente
class Paciente(models.Model):
    nome = models.CharField(
        max_lenght = 64,
        required = True,
        unique = True,
    )

    cpf = models.CharField(
        max_lenght = 11,
        required = True,
        unique = True
    )
    
    genero = models.CharField(
        max_lenght = 1,
        required = True
    )

    email = models.EmailField(
        required = True,
    )

    dt_nascimento = models.DateField(
        required = True,
    )

# Profissionais
class Especializacao(models.Model):
    nome = models.CharField(
        max_lenght = 64,
        required = True,
        unique = True
    )

    # código unico de especialidade de saúde
    tuss = models.CharField(
        max_lenght = 24,
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
    genero = models.CharField(
        max_lenght = 1,
        required = True,
    )
    email = models.EmailField(
        required = True,
    )

    dt_nascimento = models.DateField(
        required = True,
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

class Assistente(models.Model):
    nome = models.CharField(
        max_lenght = 64,
    )