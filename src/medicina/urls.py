from django.urls import path
from medicina.controllers import *

urlpatterns = [
    path("listar_consultas/", listar_consultas, name="listar_consultas"),
    path("agendar_consulta/", agendar_consulta, name="agendar_consulta"),
    
    path("reagendar_consulta/<int:id>", reagendar_consulta, name="reagendar_consulta"),
    path("cancelar_consulta/<int:id>", cancelar_consulta, name="cancelar_consulta"),
    path("realizar_consulta/<int:id>", realizar_consulta, name="realizar_consulta"),
    path("finalizar_consulta/<int:id>", finalizar_consulta, name="finalizar_consulta"),

    path("emitir_atestado/<int:id>", emitir_atestado, name="emitir_atestado"),

    path("visualizar_prontuario/<str:paciente_cpf>", visualizar_prontuario, name="visualizar_prontuario"),

    path("listar_exames/", listar_exames, name="listar_exames"),
    path("agendar_exame/", agendar_exame, name="agendar_exame"),
    path("reagendar_exame/<int:id>", reagendar_exame, name="reagendar_exame"),

]
