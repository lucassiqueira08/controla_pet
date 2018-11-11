import json
import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from servicos.models import (Atendimento, FeitoPor, AtendimentoProcClinico,
                             AtendimentoProcEstetico, ProcedimentoEstetico,
                             ProcedimentoClinico, Orcamento, TipoProcedimento)
from core.models import Menu
from cliente.models import Cliente
from usuarios.models import Funcionario


class ViewCadastroProcedimento(View):

    template = 'cadastro_procedimento.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template, context)

    def post(self, request):
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        especie = request.POST.get('especie')
        aba_procedimento = request.POST.get('aba_procedimento')

        if aba_procedimento == 'clinico':
            tipo_procedimento = request.POST.get('tipo_procedimento')

            procedimento = ProcedimentoClinico()
            procedimento.nome = nome
            procedimento.descricao = descricao
            procedimento.preco = preco.replace(",", ".")
            procedimento.especie = especie
            procedimento.id_tipo_proc = TipoProcedimento.objects.get(id=tipo_procedimento)
            procedimento.save()
        if aba_procedimento == 'estetico':
            procedimento = ProcedimentoEstetico()
            procedimento.nome = nome
            procedimento.descricao = descricao
            procedimento.preco = preco.replace(",", ".")
            procedimento.especie = especie
            procedimento.save()

        context = {
            'tipo': 'ok',
            'mensagem': 'Procedimento cadastrado com sucesso',
            'time': 5000
        }

        return HttpResponse(json.dumps(context), content_type='application/json')


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
