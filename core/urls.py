from django.urls import path

from .views import ViewIndexBemVindo, ViewIndex, ErroPermissao, ErroNaoEncontrado, ErroInterno
from .actions import get_atendimentos, get_notificacao

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path('erro_permissao',      ErroPermissao.as_view(),    name='erro_permissao'),
    path('erro_nao_encontrado', ErroNaoEncontrado.as_view(),name='erro_nao_encontrado'),
    path('erro_interno'  ,      ErroInterno.as_view()  ,    name='erro_interno'),
    path(
        'get_atendimentos', get_atendimentos
    ),
    path(
        'get_notificacao', get_notificacao
    ),
    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
