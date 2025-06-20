from django.db import models

class user(models.Model):
    usuario_1 = models.CharField(max_length=100)
    senha = models.CharField(max_length=13)

