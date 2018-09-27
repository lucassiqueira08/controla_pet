from django.urls import path

from .views import ViewCadastroProcedimento, ViewCadastroEstadia, ViewModal

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
]
