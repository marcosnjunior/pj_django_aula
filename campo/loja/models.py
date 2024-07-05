from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()

    def __str__(self):
        return self.nome
