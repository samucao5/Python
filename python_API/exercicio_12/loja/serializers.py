from rest_framework import serializers
from loja.models import cliente,produto

class cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class produto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'

