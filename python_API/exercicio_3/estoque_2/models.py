from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco= models.DecimalField(max_digits=8,decimal_places=2)
    estoque = models.IntegerField()
    ano = models.IntegerField()

    def __str__(self):
        f"nome do produto: {self.nome} \n preco do produto: {self.preco} \n estoque do produto: {self.estoque} \n ano do produto: {self.ano}"

