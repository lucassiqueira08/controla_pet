from django.urls import path

from .views import ViewCadastroAtendimento, ViewCadastroEstadia, ViewModal
from .actions import get_procedimento

urlpatterns = [
    path(
        'cadastro_estadia', ViewCadastroEstadia.as_view(),
        name='cadastro_estadia'
    ),
    path(
        'modal', ViewModal.as_view(),
        name='modal'
    ),
    path(
        'cadastro_atendimento', ViewCadastroAtendimento.as_view(),
        name='cadastro_atendimento'
    ),
    path(
        'get_procedimento', get_procedimento,
        name='get_procedimento'
    )
]
