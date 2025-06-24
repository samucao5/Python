from django.db import models

class User(models.Model):
    usuario = models.CharField(max_length=20)
    primeiro_nome = models.CharField(max_length=20)
    ultimo_nome = models.CharField(max_length=20)
    senha = models.CharField(max_length=15)


