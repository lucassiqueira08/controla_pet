from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from datetime import datetime, date

from django.views import View
from .models import Menu, MenuGrupo
from servicos.models import Atendimento, FeitoPor
from cliente.models import Cliente, Animal
from usuarios.models import Funcionario, CargoFuncionario
from django.http import HttpResponseRedirect
from gagenda.app import GCalGoogle


class BaseView(LoginRequiredMixin, View):
    redirect_field_name = 'redirect_to'
    login_url = '/usuario/login'
    permission_required = 'usuarios.Admin'
    lista_titulos = MenuGrupo.objects.filter


class ViewIndexBemVindo(BaseView):

    template = 'index_bemvindo.html'

    def get(self, request):
        context = {
            'usuario_nome': request.user.primeiro_nome.title(),
            'menu': Menu.objects.get(url= 'index')
        }
        return render(request, self.template, context)


class ViewIndex(BaseView):

    template = 'index.html'

    def get(self, request):
        atendimento = Atendimento.objects.all()
        funcionarios = Funcionario.objects.all()
        context = {
            'menu': Menu.objects.get(url= 'index'),
            'Atendimentos': atendimento,
            'Funcionarios': funcionarios,

        }
        return render(request, self.template, context)

    def post(self, request):
        if request.method == "POST":
         botao = request.POST.get('button')
         radio = request.POST.get('inlineRadioOptions')
         if botao == 'save' :
            contador= 0
            periodo= 0
            if radio == 'M':
                contador = 12 
            if radio == 'S':
                contador = 52

            if radio == 'A':
                contador = 10

            if radio == 'N':
                contador = 1
               
            for cont in range(contador):
                data = request.POST.get('dataAtendimento')+'T'+request.POST.get('HoraAtendimento')
                obssumary = request.POST.get('obs')

                #dicionario molde para o calendar
                event = {
            #-------------------------------CRIA O EVENTO--------------------------------
                  'summary': obssumary,
                  'location': 'Av. Dr. Alberto de Oliveira Lima, 254 - Real Parque, São Paulo',
                  'description': obssumary,
                #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------
                  'start': {
                    'dateTime':  data+':00', # Adição da hora com o fusorario
                    'timeZone': 'America/Sao_Paulo',
                  },
                  'end': {
                    'dateTime':  data+':00',
                    'timeZone': 'America/Sao_Paulo',
                #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------
                  },

                }
                data_nova = request.POST.get('dataAtendimento')
                hora_nova = request.POST.get('HoraAtendimento')

                google= GCalGoogle()
                gid = google.criar(event)
                funcionarios = Funcionario.objects.all()
                feito = FeitoPor()
                cliente = Cliente.objects.get(cpf= request.POST.get('cpf_cliente') )
                atendimento = Atendimento()
                atendimento.observacao = request.POST.get('obs')
              
                data_nova =  datetime.strptime(data_nova, "%Y-%m-%d").date()
                if radio == 'M':
                    periodo = periodo + 30
                if radio == 'S':
                    periodo = periodo + 7 
                if radio == 'A':
                    periodo = periodo + 365
                if radio == 'N':
                    periodo = 0             
                data_nova = date.fromordinal(data_nova.toordinal() + periodo) 
                data_nova = str(data_nova)
                data_atend = data_nova +' ' + hora_nova
                atendimento.data_solicitacao =  data_atend

                Atend_animal= Animal.objects.get(cpf_cliente=cliente, pk= request.POST.get('selectAnimal'))
                atendimento.id_animal = Atend_animal

                Responsavel = Funcionario.objects.get(cpf= request.POST.get('funcionarios'))
                atendimento.id_google_agenda = gid
                atendimento.save()
                feito.id_atendimento= atendimento
                feito.id_funcionario = Responsavel
                feito.save()
                atendimento = ''
                cliente = ''
                botao = ''

         if botao == 'edit':
            atendimento = Atendimento.objects.get(id = request.POST.get('IdEvento'))
            atendimento.observacao = request.POST.get('obsedit')
            data = request.POST.get('DataInicioedit')+'T'+request.POST.get('HoraInicioedit')+':00'
            atendimento.data_solicitacao = data
            google= GCalGoogle()
            IdGoogle = atendimento.id_google_agenda
            coment = request.POST.get('obsedit')
            google.atualizar(IdGoogle,coment,data,data)
            atendimento.save()

         if botao == 'del': 
            atendimento = Atendimento.objects.get(id = request.POST.get('IdEvento'))
            google= GCalGoogle()
            google.deletar(atendimento.id_google_agenda)
            feito = FeitoPor.objects.get(id_atendimento= request.POST.get('IdEvento'))
            feito.delete()
            atendimento.delete()


        context = {
            'menu': Menu.objects.get(url= 'index'),
            'Atendimentos': Atendimento.objects.all(),


        }
        return HttpResponseRedirect('/index')
