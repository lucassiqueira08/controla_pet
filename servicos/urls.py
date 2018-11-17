from django.urls import path
from servicos.actions import (get_tipo_procedimento, get_animais_cliente,
                              get_animal, get_diagnostico, get_tipo_exame)
from .views import (ViewCadastroProcedimento, ViewCadastroEstadia,
                    ViewModal, ViewCadastroAtendimento, ViewCadastrarDiagnostico)

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
        'cadastro_procedimento', ViewCadastroProcedimento.as_view(),
        name='cadastro_procedimento'
    ),
    path(
        'get_tipo_procedimento', get_tipo_procedimento,
        name='get_tipo_procedimento'
    ),
    path(
        'get_animais_cliente', get_animais_cliente,
        name='get_animais_cliente'
    ),
    path(
        'get_animal', get_animal,
        name='get_animal'
    ),
    path(
        'cadastrar_diagnostico', ViewCadastrarDiagnostico.as_view(),
        name='cadastrar_diagnostico'
    ),
    path(
        'get_diagnostico', get_diagnostico,
        name='get_diagnostico'
    ),
    path(
        'get_tipo_exame', get_tipo_exame,
        name='get_tipo_exame'
    ),
]
