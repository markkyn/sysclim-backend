from django.urls import path

from common.controllers import *

urlpatterns = [
    # Paciente
    path("listar_pacientes/", listar_pacientes, name="listar_pacientes"),
    path("cadastrar_paciente/", cadastrar_paciente, name="cadastrar_paciente"),

    # Profissional
    path("listar_profissionais/", listar_profissionais, name="listar_profissionais"),
    path("cadastrar_profissional/", cadastrar_profissional, name="cadastrar_profissional"),

    # Sala
    path("cadastrar_sala/", cadastrar_sala, name="cadastrar_sala"),

    # Especialidade
    path("cadastrar_especialidade/", cadastrar_especialidade, name="cadastrar_especialidade")

    #path("listar_salas/", listar_salas, name="listar_salas"),
]