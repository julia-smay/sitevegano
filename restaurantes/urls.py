from django.urls import path
from restaurantes.views import index, detalhes, buscar

urlpatterns = [
    path('', index, name = 'index'),
    path('detalhes/<int:rest_id>', detalhes, name='detalhes'),
    path('buscar', buscar, name='buscar'),
]