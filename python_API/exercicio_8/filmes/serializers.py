from rest_framework import serializers
from .models import filme

class filme_serializer(serializers.ModelSerializer):
    class Meta:
        model = filme
        fields = '__all__'

    def validate_nota(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("A nota informada foi menor que 0 ou maior que 10")
        return value
