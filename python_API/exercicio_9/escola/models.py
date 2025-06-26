from django.db import models

class turma(models.Model):
    ano = models.CharField(max_length=20)

    def __str__(self):
        return self.turma
    
class professor(models.Model):
    nome = models.CharField(max_length=32)
    ano = models.ForeignKey(turma,on_delete=models.CASCADE)

    def __str__(Self):
        return f"{self.professor} ({self.turma.ano})"


