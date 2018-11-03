from django.urls import path

from .views import ViewIndexBemVindo, ViewIndex, Erro403, Erro404, Erro500
from .actions import get_atendimentos, get_notificacao

urlpatterns = [
    path('index',      ViewIndex.as_view(), name='index'),
    path('erro_403',   Erro403.as_view(),   name='erro_403'),
    path('erro_404',   Erro404.as_view(),   name='erro_404'),
    path('erro_500',   Erro500.as_view(),   name='erro_500'),
    path(
        'get_atendimentos', get_atendimentos
    ),
    path(
        'get_notificacao', get_notificacao
    ),
    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
