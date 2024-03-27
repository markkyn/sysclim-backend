from django.urls import path

from .views import *

urlspatterns = [
    path("profissionais/all"    , list_profissional_saude, name="list_profissional_saude"),
    path("profissionais/disable", disable_profissional_saude, name="disable_profissional_saude"),
    path("profissionais/create" , create_profissional_saude, name="create_profissional_saude"),
]