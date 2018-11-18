import json
import datetime

from django.core.files.uploadedfile import TemporaryUploadedFile
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from cliente.models import FichaAnimal, Animal
from servicos.models import (Atendimento, FeitoPor, AtendimentoProcClinico,
                             AtendimentoProcEstetico, ProcedimentoEstetico,
                             ProcedimentoClinico, Orcamento, TipoProcedimento,
                             DiagnosticoAnimal, TipoDiagnostico, FichaDiagnostico,
                             Exame, TipoExame)

from core.views import BaseView
from core.models import Menu
from cliente.models import Cliente
from usuarios.models import Funcionario
from gdstorage.app import upload_animal_exame

from raven.contrib.django.raven_compat.models import client


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
            ficha_animal = FichaAnimal.objects.get(data_consulta=datetime.date.today(),
                                                   id_animal=request.POST.get('id_animal'))
        except:
            ficha_animal = FichaAnimal()

        animal = Animal.objects.get(id=request.POST.get('id_animal'))
        ficha_animal.id_animal = animal
        data_consulta = str(datetime.date.today())
        if data_consulta:
            ficha_animal.data_consulta = data_consulta
        try:
            ficha_animal.save()

        except:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Não foi possível cadastrar este diagnóstico',
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        lista_diagnostico = request.POST.getlist('diagnostico_boolean')
        for e in lista_diagnostico:
            ficha_diagnostico = FichaDiagnostico()
            diagnostico = DiagnosticoAnimal.objects.get(id=e)
            ficha_diagnostico.id_diagnostico = diagnostico
            ficha_diagnostico.id_ficha = ficha_animal
            ficha_diagnostico.save()

        ficha_animal.descricao = request.POST.get('descricao_ficha')

        file = request.FILES

        if file:
            exame = Exame()
            exame.id_animal = animal
            exame.nome = request.POST.get('nome_exame')

            if not exame.nome:
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Digite um nome de identificação para o exame',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            exame.descricao = request.POST.get('descricao_exame')
            data_realizacao = request.POST.get('data_realizacao_exame')

            if data_realizacao:
                exame.data_realizacao = datetime.datetime.strptime(data_realizacao, "%d/%m/%Y").strftime('%Y-%m-%d')

            tipo_exame = TipoExame.objects.get(id=request.POST.get('id_tipo_exame'))
            if tipo_exame:
                exame.id_tipo_exame = tipo_exame

            try:
                temp_file = TemporaryUploadedFile(name=file['exame'].name,
                                                  content_type=file['exame'].content_type,
                                                  size=file['exame'].size,
                                                  charset=file['exame'].charset)
                temp_path = temp_file.temporary_file_path()

                destination = open(temp_path, 'wb+')
                for chunk in file['exame'].chunks():
                    destination.write(chunk)
                destination.close()

                arquivo = upload_animal_exame(file['exame'], animal.pk,
                                              temp_path, exame.data_realizacao)
                exame.link_doc = arquivo
                exame.save()
            except:
                client.captureException()
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Não foi possível cadastrar este exame',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

        context = {
            'tipo': 'ok',
            'mensagem': 'Diagnostico cadastrado com sucesso',
            'time': 7000
        }
        return HttpResponse(json.dumps(context), content_type='application/json')
