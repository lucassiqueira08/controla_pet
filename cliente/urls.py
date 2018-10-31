from django.urls import path

from .views import (ViewCadastrarAnimal, ViewVisualizarAnimal,
                    ViewCadastrarCliente, ViewVisualizarCliente,
                    ViewFichaAnimal, ViewAcompanheSuaClinica,
                    ViewBuscarAnimal, ViewCadastrarDiagnostico)
                    
from .actions import get_cliente, get_animal

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
        'visualizar_animal', ViewVisualizarAnimal.as_view(),
        name='visualizar_animal'
    ),
    path(
        'visualizar_cliente', ViewVisualizarCliente.as_view(),
        name='visualizar_cliente'
    ),
    path(
        'get_cliente', get_cliente
    ),
    path(
        'acompanhe_sua_clinica', ViewAcompanheSuaClinica.as_view(),
        name='acompanhe_sua_clinica'
    ),
    path(
        'buscar_animal', ViewBuscarAnimal.as_view(),
        name='buscar_animal'
    ),
    path(
        'ficha_animal', ViewFichaAnimal.as_view(),
        name='ficha_animal'
    ),
    path(
        'cadastrar_diagnostico', ViewCadastrarDiagnostico.as_view(),
        name='cadastrar_diagnostico'
    ),
    path(
        'acompanhe_sua_clinica', ViewAcompanheSuaClinica.as_view(),
        name='acompanhe_sua_clinica'
    ),
    path(
        'get_animal/<str:cpf_cliente>/<str:nome_animal>', get_animal
    ),
]
