from django.urls import path, include
from django.contrib.auth.views import login, logout

from usuarios.views import ViewCadastroFuncionario
from .actions import get_funcionario, get_cargo

urlpatterns = [
    path('login/', login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout_url'),
    path('get_funcionario', get_funcionario, name='get_funcionario'),
    path('get_cargo', get_cargo, name='get_cargo'),
    path(
        'cadastro_funcionario/', ViewCadastroFuncionario.as_view(), name='cadastro_funcionario'
    ),
    path('accounts/', include('django.contrib.auth.urls')),
]
