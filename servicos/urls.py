from django.urls import path
from servicos.actions import get_tipo_procedimento
from .views import ViewCadastroProcedimento, ViewCadastroEstadia, ViewModal,ViewCadastroAtendimento
from servicos.actions import get_animais_cliente
from cliente.actions import get_ficha_animal
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

]
