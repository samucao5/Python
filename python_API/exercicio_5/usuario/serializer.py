from rest_framework import serializers
from .models import user

class userModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = user 
        fields = ['id','usuario','senha']

