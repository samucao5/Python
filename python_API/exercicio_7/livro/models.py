from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=40)
    autor=models.CharField(max_length=40)

    def __str__(self):
        return self.titulo
    
    
