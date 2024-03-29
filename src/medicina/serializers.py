

from rest_framework import serializers
from .models import *

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'

class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = '__all__'

class AtestadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atestado
        fields = '__all__'
