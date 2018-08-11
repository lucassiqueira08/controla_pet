from django.urls import path
from django.contrib.auth.views import login, logout

from usuarios.views import ViewEsqueceuSenha, ViewCadastrarFuncionario

urlpatterns = [
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'next_page': '/usuario/login/'}, name='logout'),

    path(
        'esqueceu_senha/', ViewEsqueceuSenha.as_view(), name='esqueceu_senha'
    ),

    path(
        'cadastrar_funcionario/', ViewCadastrarFuncionario.as_view(),
        name='cadastrar_funcionario'
    ),
]
