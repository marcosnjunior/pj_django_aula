from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome



class Fornecedor(models.Model):

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


