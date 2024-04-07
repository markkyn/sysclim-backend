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
    path("cadastrar_especialidade/", cadastrar_especialidade, name="cadastrar_especialidade"),
    
    # Escalas
    path("listar_escalas/", listar_escalas, name="listar_escalas"),
    path("cadastrar_escala/", cadastrar_escala, name="cadastrar_escala"),
    path("aplicar_escala/", aplicar_escala, name="aplicar_escala")

    #path("listar_salas/", listar_salas, name="listar_salas"),
]