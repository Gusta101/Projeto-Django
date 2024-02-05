from django.shortcuts import render


def index(request):
    context = {
        "curso": "Curso de Python com foco em Django para Fullstack",
        "titulo2": "Não sei o que escrever"
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, "contato.html")
