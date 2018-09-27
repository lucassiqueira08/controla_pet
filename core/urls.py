from django.urls import path

from .views import ViewIndex
from .views import ViewIndexBemVindo
from .actions import get_Atendimentos

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path(
        'get_Atendimentos', get_Atendimentos
    ),

    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
