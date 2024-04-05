from django.urls import path

from common.controllers import *

urlpatterns = [
    path("listar_pacientes/", listar_pacientes, name="listar_pacientes"),
    path("cadastrar_paciente/", cadastrar_paciente, name="cadastrar_paciente")
]