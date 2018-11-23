from django.urls import path

from .views import ViewCadastroProcedimento, ViewCadastroEstadia, ViewModal,ViewCadastroAtendimento

from cliente.actions import get_ficha_animal

from servicos.actions import (get_tipo_procedimento, get_animais_cliente,
                              get_animal, get_diagnostico, get_tipo_exame,
                              get_procedimento, get_pagamentos_pendentes,
                              get_animais_hospedados, get_atendimentos_pendentes, )
from .views import (ViewCadastroProcedimento, ViewCadastroEstadia,
                    ViewModal, ViewCadastroAtendimento, ViewCadastrarDiagnostico,ViewCalculoRota)

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
        'cadastrar_diagnostico', ViewCadastrarDiagnostico.as_view(),
        name='cadastrar_diagnostico'
    ),
    path(
        'calculo_rota', ViewCalculoRota.as_view(),
        name='calculo_rota'
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
        'get_diagnostico', get_diagnostico,
        name='get_diagnostico'
    ),
    path(
        'get_tipo_exame', get_tipo_exame,
        name='get_tipo_exame'
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
