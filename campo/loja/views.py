from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.


def pesquisar(request):

    resultado = Produto.objects.filter(nome__contains='banana', preco=20, quantidade__gt=0)
    return HttpResponse(resultado)


def cadastrar(request):
    print("Chegou no cadastrar tes")


def deletar(request):
    print("Chegou no deletar")


def atualizar(request):
    print('Estou no atualizar')
    return HttpResponse("Estou no atualizar")