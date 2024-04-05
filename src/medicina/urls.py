from django.urls import path
from medicina.controllers import *

urlpatterns = [
    path("listar_consultas/", listar_consultas, name="listar_consultas"),
    path("agendar_consulta/", agendar_consulta, name="agendar_consulta"),
    path("reagendar_consulta/<int:id>", reagendar_consulta, name="reagendar_consulta"),
    path("cancelar_consulta/<int:id>", cancelar_consulta, name="cancelar_consulta"),
]
