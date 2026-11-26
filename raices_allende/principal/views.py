from django.shortcuts import render
from .models import LugarTuristico, Gastronomia, Tradicion, Artesania, CulturaAficion, Galeria

def inicio(request):
    return render(request, 'principal/index.html')

def lugares(request):
    lista = LugarTuristico.objects.all()
    galeria = Galeria.objects.filter(seccion='lugares')
    contexto = {
        "titulo": "Lugares",
        "elementos": lista,
        "galeria_seccion": galeria
    }
    return render(request, 'principal/lugares.html', contexto)

def gastronomia(request):
    lista = Gastronomia.objects.all()
    galeria = Galeria.objects.filter(seccion='gastronomia')
    contexto = {
        "titulo": "Gastronomía",
        "elementos": lista,
        "galeria_seccion": galeria
    }
    return render(request, 'principal/gastronomia.html', contexto)

def tradiciones(request):
    lista = Tradicion.objects.all()
    galeria = Galeria.objects.filter(seccion='tradiciones')
    contexto = {
        "titulo": "Tradiciones",
        "elementos": lista,
        "galeria_seccion": galeria
    }
    return render(request, 'principal/tradiciones.html', contexto)

def artesanias(request):
    lista = CulturaAficion.objects.all()
    galeria = Galeria.objects.filter(seccion='artesanias')
    contexto = {
        "titulo": "Artesanías",
        "elementos": lista,
        "galeria_artesanias": galeria
    }
    return render(request, 'principal/artesanias.html', contexto)

def cultura(request):
    lista = CulturaAficion.objects.all()
    contexto = {
        "titulo": "Cultura y Aficiones",
        "elementos": lista
    }
    return render(request, 'principal/cultura.html', contexto)

def contacto(request):
    return render(request, 'principal/contacto.html')

def historia(request):
    return render(request, 'principal/historia.html')