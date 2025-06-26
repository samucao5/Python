from rest_framework import serializers
from escola.models import turma,professor

class turma_serializer(serializers.ModelSerializer):
    class Meta:
        model = turma
        fields = '__all__'

class professor_serializer(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields='__all__'