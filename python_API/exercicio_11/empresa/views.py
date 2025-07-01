from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from empresa.models import evento,participacao
from empresa.serializers import evento_serializer,participacao_serializer

class evento_api_view(generics.ListCreateAPIView):
    queryset = evento.objects.all()
    serializer_class = evento_serializer
    permission_classes = [IsAuthenticated]

class participacao_api_view(generics.ListCreateAPIView):
    queryset = participacao.objects.all()
    serializer_class = participacao_serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


