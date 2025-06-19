from django.db import models
from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8,decimal_places=2)
    estoque=models.IntegerField()

    def __str__(self):
        return f"{self.nome}, {self.preco}, {self.estoque}"
    