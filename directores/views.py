from urllib import request
from django.shortcuts import render
from .models import Peliculas, Directores

# Create your views here.


def listarPeliculas(request):
    
    lista_peliculas = Peliculas.objects.all()

    return render(
        request,
        'peliculas.html',
        context={
            'lista_peliculas': lista_peliculas
        }
    )

def listarDirectores(request):
    lista_directores = Directores.objects.all()

    return render(
        request,
        'directores.html',
        context={
            'lista_directores': lista_directores
        }
    )