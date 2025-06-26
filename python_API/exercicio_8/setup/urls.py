from django.urls import path
from filmes.views import filme_api_view

urlpatterns = [
    path('filmes/',filme_api_view.as_view())
]
