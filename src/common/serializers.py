from rest_framework import serializers

from .models import ProfissionalSaude, Enfermeiro

from medicina.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"

class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = '__all__'

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = "__all__"