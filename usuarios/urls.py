from django.urls import path
from django.contrib.auth.views import login, logout

from usuarios.views import ViewEsqueceuSenha,ViewCadastroFuncionario
from .actions import get_funcionario, get_cargo

urlpatterns = [
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
    path(
        'esqueceu_senha/', ViewEsqueceuSenha.as_view(), name='esqueceu_senha'
    ),
    path('get_funcionario', get_funcionario, name='get_funcionario'),
    path('get_cargo', get_cargo, name='get_cargo'),
    path(
        'cadastro_funcionario/', ViewCadastroFuncionario.as_view(), name='cadastro_funcionario'
    ),

]
