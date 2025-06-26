from rest_framework import generics
from .models import Livro
from .serializer import livroSerializer

class livro_api_view(generics.ListCreateAPIView):
    queryset=Livro.objects.all()
    serializer_class = livroSerializer