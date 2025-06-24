from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import userModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def status_api(request):
    return Response({"status api: ": "API online"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):
           return Response({
            "usuario": request.user.usuario,
            "id": request.user.id
           })                 
                            

@api_view(['POST'])
def criar_usuario(request):
    serializer = userModelSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'id': user.id,
            'usuario': user.usuario,
            'senha': user.senha
        },status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
