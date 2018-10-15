from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View
from .models import Menu, MenuGrupo 
from servicos.models import Atendimento,FeitoPor
from cliente.models import Cliente,Animal
from usuarios.models import Funcionario,CargoFuncionario
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
         
         if botao == 'save':
            data = request.POST.get('dataAtendimento')
            data = data[0:10]+'T'+data[11:] 
            event = {

#-------------------------------CRIA O EVENTO--------------------------------
              'summary': data,
              'location': 'Av. Dr. Alberto de Oliveira Lima, 254 - Real Parque, São Paulo',
              'description': 'A chance to hear more about Google\'s developer products.',
            #-------------------------------/CRIA O EVENTO--------------------------------

            #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------
              'start': {
                'dateTime':  data+'-03:00',
                'timeZone': 'America/Sao_Paulo',
              },
              'end': {
                'dateTime':  data+'-03:00',
                'timeZone': 'America/Sao_Paulo',
            #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------


              },

            }
            google= GCalGoogle()
            gid = google.criar(event)
            funcionarios = Funcionario.objects.all()
            feito = FeitoPor()
            cliente = Cliente.objects.get(cpf= request.POST.get('cpf') )
            atendimento = Atendimento() 
            atendimento.observacao = request.POST.get('obs')
            atendimento.data_solicitacao = request.POST.get('dataAtendimento')
            atendimento.cpf_cliente = cliente
            teste = Funcionario.objects.get(id=2)
            atendimento.id_google_agenda = gid
            atendimento.save()
            feito.id_atendimento= atendimento
            feito.id_funcionario = teste
            feito.save()
            atendimento = ''
            cliente = ''
            botao = ''

         if botao == 'edit':
            atendimento = Atendimento.objects.get(id = request.POST.get('IdEvento'))
            atendimento.observacao = request.POST.get('obsedit')
            atendimento.data_solicitacao = request.POST.get('DataInicioedit')
            atendimento.save()

         if botao == 'del':
            atendimento = Atendimento.objects.get(id = request.POST.get('IdEvento')) 
            feito = FeitoPor.objects.get(id_atendimento= request.POST.get('IdEvento'))
            feito.delete() 
            atendimento.delete()


        context = {
            'menu': Menu.objects.get(url= 'index'),
            'Atendimentos': Atendimento.objects.all(),
            
          
        }
        return HttpResponseRedirect('/index')
        

