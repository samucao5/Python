from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserModelSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
def criar_conta(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'usuario': user.usuario,
            'senha': user.senha
        },status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def token(request):
    return Response({'mensagem': 'Acesso autorizado com Token!'})

def retorno_dos_dados(request):
    return Response({
        "id": request.user.id,
        "usuario": request.user.usuario,

    })


