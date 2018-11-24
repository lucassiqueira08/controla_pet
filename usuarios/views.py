import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import Funcionario, FuncionarioAbstrato, Veterinario, User

from raven.contrib.django.raven_compat.models import client


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
        veterinario = request.POST.get('veterinario')
        login = primeiro_nome + '.' + ultimo_nome


        login_busca = User.objects.filter(login = login).first()
        cpf_busca = Funcionario.objects.filter(cpf = cpf).first()
        print(login_busca)
        if cpf_busca:
            context = {
            'tipo': 'erro',
            'mensagem': 'Cpf '+cpf+' já cadastrado!',
            'time': 5000
            }

        if login_busca:
            context = {
            'tipo': 'erro',
            'mensagem': 'Já existe um login associado à "'+login+'"',
            'time': 5000
            }
        else:
            funcionario = Funcionario()
            funcionario.apelido = apelido
            funcionario.situacao_func = situacao
            funcionario.data_nasc = data_nasc
            funcionario.primeiro_nome = primeiro_nome
            funcionario.ultimo_nome = ultimo_nome
            funcionario.login = login
            funcionario.cpf = cpf
            if equipe_sistema == 1:
                funcionario.equipe_sistema = True
            else:
                funcionario.equipe_sistema = False

            if equipe_sistema == 'Sim':
                funcionario.is_staff = True
            else:
                funcionario.is_staff = False
            funcionario.is_superuser = False
            funcionario.situacao = True
            try:
                funcionario.save()
            except ValidationError as e:
                client.captureException()
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Por favor, digite uma data válida!',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            except Exception as e:
                print(e)
                client.captureException()
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Não foi possível cadastrar esse funcionário!',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')


            if veterinario == 1:
                estado_emissor = request.POST.get('estado_emissor')
                crmv = request.POST.get('crmv')
                veterinario = Veterinario()
                if crmv:
                    veterinario.crmv = crmv
                else:
                    veterinario.crmv = '000'
                veterinario.estado_emissor = estado_emissor
                veterinario.id_funcionario = funcionario
                try:
                    veterinario.save()
                except Exception as e:
                    client.captureException()
                    context = {
                        'tipo': 'erro',
                        'mensagem': 'Não foi possível cadastrar esse veterinário!',
                        'time': 7000
                    }
                    return HttpResponse(json.dumps(context), content_type='application/json')

            context = {
                'tipo': 'ok',
                'mensagem': 'Funcionário cadastrado com sucesso',
                'time': 5000
            }
        return HttpResponse(json.dumps(context), content_type='application/json')
