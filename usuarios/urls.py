from django.urls import path
from django.contrib.auth.views import login

from usuarios.views import view_esqueceu_senha, view_login

urlpatterns = [
#    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('login/', view_login),
    path('esqueceu_senha/', view_esqueceu_senha, name='esqueceu_senha'),
]
