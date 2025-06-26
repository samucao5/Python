from rest_framework import generics
from .models import filme
from .serializers import filme_serializer

class filme_api_view(generics.ListCreateAPIView):
    queryset = filme.objects.all()
    serializer_class = filme_serializer


