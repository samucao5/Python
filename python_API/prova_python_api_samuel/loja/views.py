from django.shortcuts import render
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from loja.models import produto, compra
from loja.serializers import produto_serializer, compra_serializer

class produto_api_view(generics.ListCreateAPIView):
    queryset = produto.objects.all()
    serializer_class = produto_serializer
    permission_classes = [IsAuthenticated]

class compra_api_view(generics.ListCreateAPIView):
    queryset = compra.objects.all()
    serializer_class = compra_serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

