from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        "curso": "Curso de Python com foco em Django para Fullstack",
        "titulo2": "Não sei o que escrever",
        "produtos": produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, "contato.html")


def produto(request, pk):
    prod = Produto.objects.get(pk)
    context = {
        "produto": prod
    }
    return render(request, "produto.html", context)