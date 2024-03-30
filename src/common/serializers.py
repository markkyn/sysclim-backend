from rest_framework import serializers

from .models import *

from medicina.models import Medico

# Uso Geral
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"

class AssistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistente
        fields = "__all__"


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
        
# Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class CreatePacienteSerializer(serializers.Serializer):
    assistente_id = serializers.IntegerField()
    paciente = PacienteSerializer()
    endereco = EnderecoSerializer()

# Medico - Show
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"

# Medico - Input
class InputMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ("crm",)

# Enfermeiro - Show
class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = '__all__'

class InputEnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = ("crm",)

# Especialidade - Show
class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'


# Profissional - Show
class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = "__all__"

# Profissional - Input
class InputProfissionalSaudeSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = ProfissionalSaude
        fields = ("cpf", "nome","genero","email","dt_nascimento","ativo", "endereco")

# Profissional - Create
class CreateProfissionalSaudeSerializer(serializers.Serializer):
    assistente_id = serializers.IntegerField()
    profissional = InputProfissionalSaudeSerializer()
    cargo = serializers.CharField(max_length = 24)
    info_cargo =  serializers.DictField()

    def validate_info_cargo(self, value):
        cargo = self.initial_data.get("cargo", None)
        if cargo == "médico":
            serializer = InputMedicoSerializer(data=value)
        elif cargo == "enfermeiro":
            serializer = EnfermeiroSerializer(data=value)
        else:
            raise serializers.ValidationError("Cargo inválido.")

        if not serializer.is_valid():
            raise serializers.ValidationError(serializer.errors)
        
        return serializer.validated_data