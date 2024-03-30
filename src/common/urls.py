from django.urls import path

from .views import *

urlpatterns = [
    # Endereco
    path("endereco/all", list_endereco, name="list_endereco"), # GET
    path("endereco/create", create_endereco, name="create_endereco"), # POST
    path("endereco/<int:id>", get_endereco, name="get_endereco"), # GET

    # Assistente
    path("assistente/all", list_assistente, name = "list_assistente"), # GET
    path("assistente/create", create_assistente, name = "create_assistente"), # POST
    
    # Paciente
    path("paciente/all", list_paciente, name = "list_paciente"), # GET
    path("paciente/create", create_paciente, name = "create_paciente"), # POST
    
    # Profissionais
    path("profissionais/all", list_profissional_saude, name="list_profissional_saude"), # GET
    path("profissionais/create", create_profissional_saude, name="create_profissional_saude"), # POST
    path("profissionais/disable", disable_profissional_saude, name="disable_profissional_saude"), # GET

    # Especialidade
    path("especialidade/all", list_especialidade, name = "list_especialidade"), # GET
    path("especialidade/create", create_especialidade, name = "create_especialidade"), # POST
    path("especialidade/<int:id>", get_especialidade, name = "get_especilidade"), # GET

    # Sala
    path("sala/all", list_sala, name="list_sala"),  # GET
    path("sala/create", create_sala, name="create_sala"),  # POST
    path("sala/<int:numero>", get_sala, name="get_sala"),  # GET

]