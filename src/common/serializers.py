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

# Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class CreatePacienteSerializers(serializers.ModelSerializer):
    assistente_id = serializers.IntegerField()
    paciente = PacienteSerializer()

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"

class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = '__all__'

# Profissional
class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = "__all__"

class CreateProfissionalSaudeSerializer(serializers.Serializer):
    assistente_id = serializers.IntegerField()
    profissional = ProfissionalSaudeSerializer()
    cargo = serializers.CharField(max_length = 24)
    info_cargo =  serializers.DictField()

    def validate_info_cargo(self, value):
        cargo = self.initial_data.get("cargo", None)
        if cargo == "médico":
            serializer = MedicoSerializer(data=value)
        elif cargo == "enfermeiro":
            serializer = EnfermeiroSerializer(data=value)
        else:
            raise serializers.ValidationError("Cargo inválido.")

        if not serializer.is_valid():
            raise serializers.ValidationError(serializer.errors)
        
        return serializer.validated_data