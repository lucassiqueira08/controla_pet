from django.urls import path


from .views import ViewCadastroProcedimento, ViewCadastroEstadia, ViewAcompanheSuaClinica, ViewAnimaisEmAberto, ViewAnimaisHospedados


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

        'acompanhe_sua_clinica', ViewAcompanheSuaClinica.as_view(),
        name='acompanhe_sua_clinica'
    ),
    path(
        'animais_em_aberto', ViewAnimaisEmAberto.as_view(),
        name='animais_em_aberto'
    ),
    path(
        'animais_hospedados', ViewAnimaisHospedados.as_view(),
        name='animais_hospedados'
    ),

=======
        'modal', ViewModal.as_view(),
        name='modal'
    ),

]
