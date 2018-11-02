from django.urls import path
from django.contrib.auth.views import login, logout

from usuarios.views import ViewEsqueceuSenha
from .actions import get_funcionario

urlpatterns = [
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
    path(
        'esqueceu_senha/', ViewEsqueceuSenha.as_view(), name='esqueceu_senha'
    ),
    path('get_funcionario', get_funcionario, name='get_funcionario'),
]
