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