from django.urls import path
from medicina.controllers import *

urlpatterns = [
    path("listar_consultas/", listar_consultas, name="listar_consultas"),
    path("agendar_consulta/", agendar_consulta, name="agendar_consulta"),

]
