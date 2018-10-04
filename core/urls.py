from django.urls import path

from .views import ViewIndex
from .views import ViewIndexBemVindo
from .actions import get_Atendimentos, get_notificacao

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path(
        'get_Atendimentos', get_Atendimentos
    ),
    path(
        'get_notificacao', get_notificacao
    ),
    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
