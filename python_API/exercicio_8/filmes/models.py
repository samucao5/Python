from django.db import models

class filme(models.Model):
    titulo = models.CharField(max_length=40)
    ano = models.IntegerField()
    nota = models.DecimalField(max_length=10.00,max_digits=4,decimal_places=2)

    def __str__ (self):
        return self.filme