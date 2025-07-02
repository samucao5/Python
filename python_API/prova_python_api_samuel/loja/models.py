from django.db import models
from django.contrib.auth.models import User

class produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_em_estoque = models.IntegerField()

    def __str__(self):
        return f"nome do produto:{self.nome} \n descrição: {self.descricao}\n preço: {self.preco}\n estoque: {self.quantidade_em_estoque}"
    
class compra(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    produto_1 = models.ForeignKey(produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.produto_1.nome}"
    
