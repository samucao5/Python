from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from livro.models import categoria, livro_1
from livro.serializers import livro_1_serializer, categoria_serializer

class livro_1_api_view(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = livro_1.objects.all()
    serializer_class = livro_1_serializer

class categoria_api_view(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = categoria.objects.all()
    serializer_class = categoria_serializer



