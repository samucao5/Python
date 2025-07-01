from django.db import models
from django.contrib.auth.models import User

class evento(models.Model):
    nome = models.CharField(max_length=100)
    vagas = models.IntegerField()

    def __Str__(self):
        return f"{self.nome} (vagas restantes: {self.vagas})"

class participacao(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    evento_2 = models.ForeignKey(evento,on_delete=models.CASCADE)
    data_partipacao = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return f"{self.usuario.username} - {self.evento_2.nome}"

