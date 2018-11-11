from django.shortcuts import render
from django.views import View


class ViewEsqueceuSenha(View):

    template = 'esqueceu_senha.html'

    def get(self, request):
        return render(request, self.template)


class ViewCadastroFuncionario(View):
    template = 'cadastro_funcionario.html'

    def get(self, request):
        context = {
        }

        return render(request, self.template, context)
