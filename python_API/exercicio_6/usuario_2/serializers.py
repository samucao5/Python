from rest_framework import serializers
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','usuario','primeiro_nome','ultimo_nome','senha']

