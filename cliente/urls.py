from django.urls import path

from .views import ViewCadastrarAnimal, ViewVisualizacaoAnimal

urlpatterns = [
    path(
        'cadastrar_animal', ViewCadastrarAnimal.as_view(),
        name='cadastrar_animal'
    ),

    path(
        'visualizar_animal', ViewVisualizacaoAnimal.as_view(),
        name='visualizar_animal'
    ),
]
