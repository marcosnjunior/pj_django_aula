from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pesquisar(request):
    print("Opa Chegou aqui")
    return HttpResponse("Estou no Pesquisar")


def cadastrar(request):
    print("Chegou no cadastrar")


def deletar(request):
    print("Chegou no deletar")


def atualizar(request):
    print('Estou no atualizar')
    return HttpResponse("Estou no atualizar")