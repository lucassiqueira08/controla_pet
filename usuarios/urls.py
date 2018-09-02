from django.urls import path
from django.contrib.auth.views import login, logout

from usuarios.views import ViewEsqueceuSenha

urlpatterns = [
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),

    path(
        'esqueceu_senha/', ViewEsqueceuSenha.as_view(), name='esqueceu_senha'
    ),
]
