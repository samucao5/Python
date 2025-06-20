from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import produtoModelSerializer


@api_view(['POST'])
def criar_produto(request):
    serializer = produtoModelSerializer(data=request.data)
    if serializer.is_valid():
        produto = serializer.save()
        return Response({
            'id': produto.id,
            'nome do produto': produto.nome,
            'preco do produto': produto.preco,
            'estoque do produto': produto.estoque,
            'ano do produto': produto.ano
        },status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




