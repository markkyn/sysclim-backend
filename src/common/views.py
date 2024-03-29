from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from common.models import *
from .serializers import *

# Endereco
@api_view(['POST'])
def create_endereco(request):
    endereco_serializer = EnderecoSerializer(data=request.data)

    if endereco_serializer.is_valid():
        try:
            endereco = EnderecoSerializer.objects.create(
                rua = endereco_serializer.validated_data[""],
                numero = endereco_serializer.validated_data[""],
                complemento = endereco_serializer.validated_data[""],
                estado = endereco_serializer.validated_data["estado"],
                cidade = endereco_serializer.validated_data["cidade"],
                cep = endereco_serializer.validated_data["cidade"],
            )



            return Response({"message":"Endereço Cadastrado com sucesso!"})
        except:
            return Response({"message":"Ocorreu um erro desconhecido, por favor contate a equipe técnica"})


    return Response()

@api_view(['GET'])
def get_endereco(request, id):
    try:
        endereco = Endereco.objects.get(id = id)

        endereco_serializer = EnderecoSerializer(endereco)

        return Response(endereco_serializer.data)
    
    except Endereco.DoesNotExist:
        return Response({"message": "Não existe um Endereço com esses identificador"})

@api_view(['GET'])
def list_endereco(request):
    pass

# Assistente
@api_view(['POST'])
def create_assistente(request):
    pass

@api_view(['GET'])
def list_assistente(request):
    pass

@api_view(['PUT'])
def disable_assistente(request):
    pass

# Paciente
@api_view(['GET'])
def list_paciente(request):
    pass

@api_view(['POST'])
def create_paciente(request):
    """
        Cria um Paciente:

        {
            "assistente": 04511800545,
            "paciente" : {
                "nome": "Marcos Gabriel",
                "cpf": "12345678901",
                "genero": "M",
                "email" :"marcos.gabriel@email.com",
                "dt_nascimento": "01/01/2001",
                "endereco": {
                    "rua":"",
                    "bairro":"",
                    "numero": "234",
                    "complemento": "",
                    ""
                }
            }
        }

    """
    return Response()

# Profissionais de Saude
@api_view(['POST'])
def create_profissional_saude(request):
    """
        Cria um Profissional de Saude:

        {
            "assistente_id":1,
            "profissional":{
                "nome":"Marcos Gabriel",
                "cpf":"12345678901",
                "genero":"M",
                "email":"marcos.gabriel@example.com",
                "dt_nascimento":"01/01/2001",
                "endereco":{
                    "rua":"Rua Passarinho Verde",
                    "bairro":"Floresta Azul",
                    "numero":"123B2",
                    "complemento":null,
                    "estado":"SE",
                    "cidade":"Aracaju",
                    "cep":"49040260"
                }
            },
            "cargo":"médico",
            "info_cargo":{
                "crm":"155489897"
            }
        }
    """
    
    profissional_input = CreateProfissionalSaudeSerializer(data = request.data)

    if profissional_input.is_valid():
        dados_profissional = profissional_input.validated_data["profissional"]
        cargo = profissional_input.validated_data["cargo"]
        info_cargo = profissional_input.validate_info_cargo["info_cargo"]

        profissional = ProfissionalSaude.objects.create(
            cpf  = dados_profissional["cpf"],
            nome = dados_profissional["nome"],
            genero = dados_profissional["genero"],
            email = dados_profissional["email"],
            dt_nascimento = dados_profissional["dt_nascimento"],
            cargo = cargo,
            ativo = True
        )

        if cargo == "médico":
            Medico.objects.create(
                crm = info_cargo["coren"],
                profissional = profissional 
            )
        elif cargo == "enfermeiro":
            Enfermeiro.objects.create(
                coren = info_cargo["coren"],
                profissional = profissional
            )

        return Response({"message": "Profissional de saúde criado com sucesso!"}, status=status.HTTP_201_CREATED)
    else:
        return Response(profissional_input.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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
