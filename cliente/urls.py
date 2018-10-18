from django.urls import path

from .views import ViewCadastrarAnimal, ViewVisualizarAnimal, ViewCadastrarCliente, ViewFichaAnimal, ViewAcompanheSuaClinica, ViewBuscarAnimal, ViewCadastrarDiagnostico, Viewteste_ajax, valida_usuario
from .actions import get_cliente
from django.conf.urls import url

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
        'teste_ajax', Viewteste_ajax.as_view(),
        name='teste_ajax'
    ),
    url(
        r'^valida_usuario/$', valida_usuario,
        name='valida_usuario'
    ),
]
