from django.urls import path

from servicos.actions import (get_tipo_procedimento, get_procedimento,
                              get_animais_hospedados, get_atendimentos_pendentes,
                              get_pagamentos_pendentes)
from .views import (ViewCadastroProcedimento, ViewCadastroEstadia, ViewModal,
                    ViewCadastroAtendimento)

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
        'get_procedimento', get_procedimento,
        name='get_procedimento'
    ),
    path(
        'get_animais_hospedados', get_animais_hospedados,
        name='get_animais_hospedados'
    ),
    path(
        'get_atendimentos_pendentes', get_atendimentos_pendentes,
        name='get_atendimentos_pendentes'
    ),
    path(
        'get_pagamentos_pendentes', get_pagamentos_pendentes,
        name='get_pagamentos_pendentes'
    ),
]
