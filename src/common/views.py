from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models import *
from .serializers import *

# Uso Geral

# Paciente
def create_paciente(request):
    Paciente.objects.create(
        nome = request.nome,
        cpf = request.cpf,
        
    )    
    return Response()

# Profissionais
@api_view(['POST'])
def create_profissional_saude(request):
    """
        Cria um Profissional de Saude
    """

    return Response()

@api_view(['POST'])
def disable_profissional_saude(request):
    """
        Desabilita o Profissional de Saude
    """
    return Response()

@api_view(['GET'])
def list_profissional_saude(request):
    """
        Retorna todos os Profissionais de Saude
    """
    profissionais = ProfissionalSaude.objects.all().order_by()
    serializer = ProfissionalSaudeSerializer(profissionais, many = True)
    
    return Response(serializer.data)
    