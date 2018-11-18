import json
import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from cliente.models import FichaAnimal, Animal
from servicos.models import (Atendimento, FeitoPor, AtendimentoProcClinico,
                             AtendimentoProcEstetico, ProcedimentoEstetico,
                             ProcedimentoClinico, Orcamento, TipoProcedimento,
                             DiagnosticoAnimal, TipoDiagnostico, FichaDiagnostico,
                             Estadia)
from core.views import BaseView
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
        }
        return render(request, self.template, context)

    def post(self, request):
        observacao       = request.POST.get('observacao')
        data_inicio      = request.POST.get('data_inicio')
        data_fim         = request.POST.get('data_fim')
        data_solicitacao = request.POST.get('data_solicitacao')
        valor_diaria     = request.POST.get('valor_diaria')
        id_animal        = request.POST.get('id_animal')

        estadia = Estadia()
        estadia.observacao       = observacao
        estadia.data_inicio      = data_inicio
        estadia.data_fim         = data_fim
        estadia.data_solicitacao = data_solicitacao
        estadia.valor_diaria     = valor_diaria
        estadia.data_solicitacao = datetime.datetime.now()
        estadia.id_animal        = Animal.objects.get(id = id_animal)
        estadia.save()

        context = {
            'tipo': 'ok',
            'mensagem': 'Estadia cadastrado com sucesso',
            'time': 5000
        }

        return HttpResponse(json.dumps(context), content_type='application/json')

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


class ViewCadastrarDiagnostico(BaseView):

    template = 'cadastrar_diagnostico.html'

    def get(self, request):
        tipo_diagnostico = TipoDiagnostico.objects.all()
        context = {
            'tipos_diagnostico': tipo_diagnostico
        }
        return render(request, self.template, context)

    def post(self, request):
        try:
            ficha_animal = FichaAnimal.objects.get(data_consulta=datetime.date, id_animal=request.POST.get('id_animal'))
        except:
            ficha_animal = FichaAnimal()

        animal = Animal()
        ficha_animal.id_animal = animal.pk
        ficha_animal.data_consulta = datetime.date
        ficha_animal.descricao = request.POST.get('diagnostico_especifico')
        try:
            ficha_animal.save()

            ficha_diagnostico = FichaDiagnostico()
            ficha_diagnostico.id_ficha = ficha_animal
            ficha_diagnostico.id_diagnostico
        except:
            context={}
