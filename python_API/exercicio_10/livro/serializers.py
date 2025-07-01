from rest_framework import serializers
from livro.models import categoria, livro_1

class categoria_serializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class livro_1_serializer(serializers.ModelSerializer):
    class Meta:
        model = livro_1
        fields = '__all__'

