
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from common.models import *
from medicina.models import *
from medicina.serializers import *

@api_view(['GET'])
def list_consultas(request):
    consultas = Consulta.objects.all()
    serializer = ConsultaSerializer(consultas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_consulta(request):
    serializer = ConsultaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_consulta(request, pk):
    try:
        consulta = Consulta.objects.get(pk=pk)
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)
    except Consulta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_exames(request):
    exames = Exame.objects.all()
    serializer = ExameSerializer(exames, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_exame(request):
    serializer = ExameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_exame(request, pk):
    try:
        exame = Exame.objects.get(pk=pk)
        serializer = ExameSerializer(exame)
        return Response(serializer.data)
    except Exame.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_prontuarios(request):
    prontuarios = Prontuario.objects.all()
    serializer = ProntuarioSerializer(prontuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_prontuario(request):
    serializer = ProntuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_prontuario(request, pk):
    try:
        prontuario = Prontuario.objects.get(pk=pk)
        serializer = ProntuarioSerializer(prontuario)
        return Response(serializer.data)
    except Prontuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_atestados(request):
    atestados = Atestado.objects.all()
    serializer = AtestadoSerializer(atestados, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_atestado(request):
    serializer = AtestadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_atestado(request, pk):
    try:
        atestado = Atestado.objects.get(pk=pk)
        serializer = AtestadoSerializer(atestado)
        return Response(serializer.data)
    except Atestado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
