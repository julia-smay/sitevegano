from django.shortcuts import render, get_object_or_404, redirect
from restaurantes.models import Restaurante


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    restaurantes = Restaurante.objects.all()
    return render(request, 'restaurantes/index.html', {"cards": restaurantes})

def detalhes(request, rest_id):
    restaurante = get_object_or_404(Restaurante, pk=rest_id)
    return render(request, 'restaurantes/detalhes.html', {'restaurante': restaurante})

def buscar(request):
    restaurantes = Restaurante.objects.all() 
    
    if "buscar" in request.GET:
        if not request.user.is_authenticated:
            return redirect('login')

        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            restaurantes = restaurantes.filter(nome__icontains=nome_a_buscar)
    
    return render(request, "restaurantes/buscar.html", {"cards": restaurantes})