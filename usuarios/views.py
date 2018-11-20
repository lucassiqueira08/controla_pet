from django.shortcuts import render
from django.views import View
from .models import Funcionario, FuncionarioAbstrato
from django.http import HttpResponse
import json


class ViewEsqueceuSenha(View):

    template = 'esqueceu_senha.html'

    def get(self, request):
        return render(request, self.template)

class ViewCadastroFuncionario(View):

    template = 'cadastro_funcionario.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        apelido = request.POST.get('apelido')
        cpf = request.POST.get('cpf')
        data_nasc = request.POST.get('data_nasc')
        id_cargo = request.POST.get('id_cargo')
        situacao = request.POST.get('situacao')
        equipe_sistema = request.POST.get('equipe_sistema')

        funcionario = Funcionario()
        funcionario.apelido = apelido
        funcionario.situacao_func = situacao
        funcionario.data_nasc = data_nasc
        funcionario.equipe_sistema = equipe_sistema
        funcionario.cpf = cpf

        funcionario.primeiro_nome = primeiro_nome
        funcionario.ultimo_nome = ultimo_nome
        funcionario.login = primeiro_nome + '.' + ultimo_nome
        if equipe_sistema == 'Sim':
            funcionario.is_staff = True
        if equipe_sistema == 'Não':
            funcionario.is_staff = False
        funcionario.is_superuser = False
        funcionario.situacao = True

        funcionario.save()

        context = {
            'tipo': 'ok',
            'mensagem': 'Funcionário cadastrado com sucesso',
            'time': 5000
        }
        return HttpResponse(json.dumps(context), content_type='application/json')
