from rest_framework import serializers
from .models import produto

class produtoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ["id","nome","preco","estoque","ano"]

    def validate_ano(self, value):
        if value > 2025:
            raise serializers.ValidationError("nao pode ser maior que 2025")
        return value


    def validate_estoque(self,value):
        if value <= 0:
            raise serializers.ValidationError("o estoque tem que ser maior que zero")
        return value