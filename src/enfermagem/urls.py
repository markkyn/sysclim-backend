from django.urls import path, include

from enfermagem.controllers import *

urlpatterns = [
    path('listar_vacinas/', listar_vacinas, name="listar_vacinas"),	
    path('cadastrar_vacina/', cadastrar_vacina, name="cadastrar_vacina"),

    path('aplicar_vacina/<str:paciente_cpf>/', aplicar_vacina, name="aplicar_vacina")
]