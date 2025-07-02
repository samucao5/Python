from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome
class produto(models.Model):
    produto_nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    cliente_1 = models.ForeignKey(cliente,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto_nome} (nome do cliente: {self.cliente_1.nome})"
    
    