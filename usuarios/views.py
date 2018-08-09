from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View


class BaseView(LoginRequiredMixin, PermissionRequiredMixin, View):

    redirect_field_name = 'redirect_to'
    login_url = '/usuario/login'
    permission_required = 'usuarios.Admin'


class ViewEsqueceuSenha(View):

    template = 'esqueceu_senha.html'

    def get(self, request):
        return render(request, self.template)


class ViewCadastrarFuncionario(View):

    template = 'cadastro_funcionario.html'

    def get(self, request):
        return render(request, self.template)
