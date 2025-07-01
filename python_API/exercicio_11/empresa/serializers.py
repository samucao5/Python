from rest_framework import serializers
from empresa.models import evento, participacao

class evento_serializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'

class participacao_serializer(serializers.ModelSerializer):
    class Meta:
        model = participacao
        fields = '__all__'
        read_only_fields = ['usuario','data_inscricao']

    def validate(self,data):
        evento_2 = data['evento_2']
        if evento_2.vagas <= 0:
            raise serializers.ValidationError("não há mais vagas disponiveis para este curso.")
        return data
    
    def create(self,validated_data):
            evento_2 = validated_data['evento_2']
            evento_2.vagas -= 1
            evento_2.save()
            return super().create(validated_data)
