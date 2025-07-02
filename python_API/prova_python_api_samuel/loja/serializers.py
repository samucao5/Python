from rest_framework import serializers
from loja.models import produto,compra

class produto_serializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'

    def validate(self,validated_data):
        estoque = validated_data['quantidade_em_estoque']
        if estoque < 1:
            raise serializers.ValidationError("a quantidade tem que ser maior que 0")
        
class compra_serializer(serializers.ModelSerializer):
    class Meta:
        model = compra
        fields = '__all__'
        read_only_fields = ['usuario', 'data_compra']
    



    def validate(self,validated_data):
        estoque = validated_data['produto_1']
        quant_a = validated_data['quantidade']

        if quant_a <= 0:
            raise serializers.ValidationError("a quantidade do produto deve ser maior que 0")

        if quant_a > estoque.quantidade_em_estoque:
            raise serializers.ValidationError("o produto acabou")
        
    def create(self,validated_data):
        quant = validated_data['produto_1']
        quant_a = validated_data['quantidade']
        quant.quantidade_em_estoque -= quant_a
        quant.save()
        return super().create(validated_data)
