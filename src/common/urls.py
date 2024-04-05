from django.urls import path

from common.controllers import *

urlpatterns = [
    path("listar_pacientes/", listar_pacientes, name="listar_pacientes"),
    path("cadastrar_paciente/", cadastrar_paciente, name="cadastrar_paciente"),

    path("listar_profissionais/", listar_profissionais, name="listar_profissionais"),
    path("cadastrar_profissional/", cadastrar_profissional, name="cadastrar_profissional"),
    #path("cadastrar_endereco", cadastrar_endereco, name="cadastrar_endereco"),

    path("listar_salas/", listar_salas, name="listar_salas"),
    path("cadastrar_sala/", cadastrar_sala, name="cadastrar_sala"),
]