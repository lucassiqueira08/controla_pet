from django.urls import path

from .views import ViewCadastrarAnimal, ViewVisualizacaoAnimal, ViewCadastrarCliente
from .actions import get_cliente

urlpatterns = [
    path(
        'cadastrar_cliente', ViewCadastrarCliente.as_view(),
        name='cadastrar_cliente'
    ),
    path(
        'cadastrar_animal', ViewCadastrarAnimal.as_view(),
        name='cadastrar_animal'
    ),

    path(
        'visualizar_animal', ViewVisualizacaoAnimal.as_view(),
        name='visualizar_animal'
    ),
    path(
        'visualizar_animal', ViewVisualizacaoAnimal.as_view(),
        name='visualizar_animal'
    ),
    path(
        'get_cliente', get_cliente
    ),
]
