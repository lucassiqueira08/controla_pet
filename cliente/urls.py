from django.urls import path

from .views import ViewCadastrarAnimal, ViewVisualizacaoAnimal, ViewCadastrarCliente, ViewFichaAnimal
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
    path(
        'ficha_animal', ViewFichaAnimal.as_view(),
        name='visualizar_animal'
    ),
]
