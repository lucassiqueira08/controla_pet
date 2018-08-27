from django.urls import path

from .views import ViewCadastroProcedimento

urlpatterns = [
    path(
        'cadastro_procedimento', ViewCadastroProcedimento.as_view(),
        name='cadastro_procedimento'
    ),
]
