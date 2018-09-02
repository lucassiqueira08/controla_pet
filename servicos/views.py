import json
import datetime

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, QueryDict

from servicos.models import (Atendimento, FeitoPor, AtendimentoProcClinico,
                             AtendimentoProcEstetico, ProcedimentoEstetico,
                             ProcedimentoClinico, Orcamento)
from core.models import Menu, MenuGrupo
from cliente.models import Cliente
from usuarios.models import Funcionario


class ViewCadastroEstadia(View):

    template = 'cadastro_estadia.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url='cadastro_estadia')
        }
        return render(request, self.template, context)

    def post(self, request):
        context = {
            'menu': Menu.objects.get(url='cadastro_estadia')
        }
        return render(request, self.template)

class ViewModal(View):

    template = 'modal_orcamento.html'

    def get(self, request):
        return render(request, self.template)

class ViewCadastroAtendimento(View):

    template = 'cadastro_atendimento.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        actual_date = datetime.datetime.now()
        data = json.loads(request.body)
        cliente = Cliente.objects.get(pk=data['cpf_cliente'])
        funcionario = Funcionario.objects.get(pk=data['funcionario'])

        orcamento = Orcamento()
        orcamento.preco_final = data['orcamento']
        orcamento.save()

        atendimento = Atendimento()

        atendimento.cpf_cliente = cliente
        atendimento.observacao = 'algo'
        atendimento.data_solicitacao = actual_date
        atendimento.id_orcamento = orcamento
        atendimento.save()

        for item in data['procedimentos']:
            if item['model'] == 'servicos.procedimentoestetico':
                atendimento_estetico = ProcedimentoEstetico.objects.get(pk=item['pk'])

                atendimento_proc_estetico = AtendimentoProcEstetico()
                atendimento_proc_estetico.id_proc_estetico = atendimento_estetico
                atendimento_proc_estetico.id_atendimento = atendimento
                atendimento_proc_estetico.save()
                continue

            atendimento_clinico = ProcedimentoClinico.objects.get(pk=item['pk'])
            atendimento_proc_clinico = AtendimentoProcClinico()
            atendimento_proc_clinico.id_proc_clinico = atendimento_clinico
            atendimento_proc_clinico.id_atendimento = atendimento
            atendimento_proc_clinico.save()

        feito_por = FeitoPor()
        feito_por.id_atendimento = atendimento
        feito_por.id_funcionario = funcionario
        feito_por.save()
        return HttpResponse(data['procedimentos'], content_type='application/json')
