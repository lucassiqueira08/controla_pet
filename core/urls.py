from django.urls import path

from .views import ViewIndexBemVindo, ViewIndex
from .actions import get_atendimentos, get_notificacao

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path(
        'get_atendimentos', get_atendimentos
    ),
    path(
        'get_notificacao', get_notificacao
    ),
    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
