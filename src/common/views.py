from django.shortcuts import render
from django.contrib.auth import authenticate, logout

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from common.models import *
from .serializers import *


# Autenticação
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
        return Response({"success": "Logout bem-sucedido."}, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Erro durante o logout."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Endereco
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_endereco(request):
    endereco_serializer = EnderecoSerializer(data=request.data)

    if endereco_serializer.is_valid():
        try:
            endereco = Endereco.objects.create(
                rua = endereco_serializer.validated_data["rua"],
                numero = endereco_serializer.validated_data["numero"],
                bairro = endereco_serializer.validated_data["bairro"],
                complemento = endereco_serializer.validated_data["complemento"],
                estado = endereco_serializer.validated_data["estado"],
                cidade = endereco_serializer.validated_data["cidade"],
                cep = endereco_serializer.validated_data["cidade"],
            )

            return Response({"message":"Endereço cadastrado com sucesso!"})
        except Exception as e:
            return Response({
                "message":"Ocorreu um erro desconhecido, por favor contate a equipe técnica",
                "errors": str(e)
            })
    else:
        return Response({"message":"O formato do endereço está incorreto, realize a criação com o endereço correto"})

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
    enderecos = Endereco.objects.all()
    
    endereco_serializer = EnderecoSerializer(enderecos, many=True)

    return Response(endereco_serializer.data)

# Sala
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_sala(request):
    try:
        salas = Sala.objects.all()
        serializer = SalaSerializer(salas, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": "Erro ao listar salas", "errors": str(e)})

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_sala(request):
    serializer = SalaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Sala criada com sucesso", "sala": serializer.data}, status=201)
    else:
        return Response({"message": "Erro ao criar sala", "errors": serializer.errors})

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_sala(request, numero):
    try:
        sala = Sala.objects.get(numero=numero)
        serializer = SalaSerializer(sala)
        return Response(serializer.data)
    except Sala.DoesNotExist:
        return Response({"message": "Sala não encontrada"}, status=404)
    except Exception as e:
        return Response({"message": "Erro ao buscar sala", "errors": str(e)})


# Assistente
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_assistente(request):
    assistente_serializer = AssistenteSerializer(data=request.data)

    if assistente_serializer.is_valid():
        try:
            assistente = Assistente.objects.create(
                nome = assistente_serializer.validated_data["nome"]
            )

            return Response({
                "message":"Assistente cadastrado com sucesso!",
                "assistente_id": assistente.id
            })
        except Exception as e:
            return Response({
                "message":"Ocorreu um erro desconhecido, por favor contate a equipe técnica",
                "errors": str(e)
            })
    else:
        return Response({"message":"O formato do endereço está incorreto, realize a criação com o endereço correto"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_assistente(request):
    assistentes = Assistente.objects.all()

    assistente_serializer = AssistenteSerializer(assistentes, many = True)

    return Response(assistente_serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def disable_assistente(request):
    # TODO: não tenho certeza se PUT seria a melhor opção para modificar o ativo do assistente
    pass

# Paciente
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_paciente(request):
    try:
        pacientes = Paciente.objects.all()

        paciente_serializer = PacienteSerializer(pacientes, many = True)
        return Response(paciente_serializer.data)
    except: 
        return Response({"message": "Erro Inesperado, contate a equipe técnica"})

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_paciente(request):
    """
        Cria um Paciente:

        {
            "assistente_id": 1,
            "paciente" : {
                "nome": "Marcos Gabriel",
                "cpf": "12345678901",
                "genero": "M",
                "email" :"marcos.gabriel@email.com",
                "dt_nascimento": "2001-01-01"
            },
            "endereco": {
                    "rua":"Rua Joaquina",
                    "bairro":"Coringuinha",
                    "numero": "234",
                    "complemento": null,
                    "cidade": "Aracaju",
                    "estado": "SE"
            }
        }

    """
    paciente_input = CreatePacienteSerializer(data = request.data)
    
    if paciente_input.is_valid():
        try:
            assistente_id = paciente_input.validated_data["assistente_id"]
            dados_paciente = paciente_input.validated_data["paciente"]
            endereco = paciente_input.validated_data["endereco"]
        
            paciente = Paciente.objects.create(
                created_by = Assistente.objects.get(id = assistente_id),
                nome = dados_paciente["nome"],
                cpf = dados_paciente["cpf"],
                genero = dados_paciente["genero"],
                email = dados_paciente["email"],
                dt_nascimento = dados_paciente["dt_nascimento"]
            )

            endereco = Endereco.objects.create(
                rua = endereco["rua"],
                numero = endereco["numero"],
                bairro = endereco["bairro"],
                complemento = endereco["complemento"],
                estado = endereco["estado"],
                cidade = endereco["cidade"],
                cep = endereco["cidade"],
            )

            return Response({
                "message": "Pacinete Criado com sucesso",
                "paciente_cpf": paciente.cpf,
                "endereco_id": endereco.id
            })
        
        except Assistente.DoesNotExist:
            return Response({
                "message":"O assistente não existe",
                "errors": str(e)
            })

        except Exception as e:
            return Response({
                "message":"Ocorreu um erro desconhecido, por favor contate a equipe técnica",
                "errors": str(e)
            })
    else:
        return Response({
            "message": "Formato Inválido",
            "errors": paciente_input.errors 
        })

# Profissionais de Saude
@permission_classes([IsAuthenticated])
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
        info_cargo = profissional_input.validated_data["info_cargo"] 

        profissional = ProfissionalSaude.objects.create(
            cpf  = dados_profissional["cpf"],
            nome = dados_profissional["nome"],
            genero = dados_profissional["genero"],
            email = dados_profissional["email"],
            dt_nascimento = dados_profissional["dt_nascimento"],
            endereco = Endereco.objects.create(
                rua = dados_profissional["endereco"].get("rua", None),
                bairro = dados_profissional["endereco"].get("bairro", None),
                numero = dados_profissional["endereco"].get("numero", None),
                complemento = dados_profissional["endereco"].get("complemento", None),
                estado = dados_profissional["endereco"].get("estado", None),
                cidade = dados_profissional["endereco"].get("cidade", None),
                cep = dados_profissional["endereco"].get("cep", None),
            ),
            cargo = cargo,
            ativo = True
        )

        if cargo == "médico":
            Medico.objects.create(
                crm = info_cargo["crm"],
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

@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def disable_profissional_saude(request):
    """
        Desabilita o Profissional de Saude
    """
    return Response()

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_profissional_saude(request):
    """
        Retorna todos os Profissionais de Saude
    """
    profissionais = ProfissionalSaude.objects.all().order_by()
    serializer = ProfissionalSaudeSerializer(profissionais, many = True)
    
    return Response(serializer.data)


# Especialidade
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_especialidade(request):
    try:
        especialidades = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": "Erro ao listar especialidades", "errors": str(e)})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_especialidade(request):
    serializer = EspecialidadeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Especialidade criada com sucesso", "especialidade": serializer.data}, status=201)
    else:
        return Response({"message": "Erro ao criar especialidade", "errors": serializer.errors})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_especialidade(request, tuss):
    try:
        especialidade = Especialidade.objects.get(tuss=tuss)
        serializer = EspecialidadeSerializer(especialidade)
        return Response(serializer.data)
    except Especialidade.DoesNotExist:
        return Response({"message": "Especialidade não encontrada"}, status=404)
    except Exception as e:
        return Response({"message": "Erro ao buscar especialidade", "errors": str(e)})