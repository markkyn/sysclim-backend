from django.urls import path

from .views import *

urlpatterns = [
    # Endereco
    path("endereco/all", list_endereco, name="list_endereco"),
    path("endereco/create", create_endereco, name="create_endereco"),
    path("endereco/get/<int:id>", get_endereco, name="get_endereco"),

    # Assistente
    path("assistente/all", list_assistente, name = "list_assistente"),
    path("assistente/create", create_assistente, name = "create_assistente"),

    # Paciente
    path("paciente/all", list_paciente, name = "list_paciente"),

    # Profissionais
    path("profissionais/all", list_profissional_saude, name="list_profissional_saude"),
    path("profissionais/create", create_profissional_saude, name="create_profissional_saude"),
    path("profissionais/disable", disable_profissional_saude, name="disable_profissional_saude"),
]