from django.urls import path
from servicos.actions import get_tipo_procedimento
from .views import ViewCadastroProcedimento, ViewCadastroEstadia, ViewModal,ViewCadastroAtendimento

urlpatterns = [
    path(
        'cadastro_procedimento', ViewCadastroProcedimento.as_view(),
        name='cadastro_procedimento'
    ),
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
        'get_tipo_procedimento', get_tipo_procedimento,
        name='get_tipo_procedimento'
    ),
]
