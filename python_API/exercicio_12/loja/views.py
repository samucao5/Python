from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from loja.models import cliente,produto
from loja.serializers import cliente_serializer,produto_Serializer

class cliente_api_view(generics.ListCreateAPIView):
    queryset = cliente.objects.all()
    serializer_class = cliente_serializer
    permission_classes = [IsAuthenticated]

class produto_api_view(generics.ListCreateAPIView):
    queryset = produto.objects.all()
    serializer_class = produto_Serializer
    permission_classes = [IsAuthenticated]

