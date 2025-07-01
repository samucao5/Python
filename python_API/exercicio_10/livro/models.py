from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class livro_1(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} {self.autor} ({self.categoria.nome})"
