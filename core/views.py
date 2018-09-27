from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from .models import Menu, MenuGrupo 
from servicos.models import Atendimento
from cliente.models import Cliente


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
        context = {
            'menu': Menu.objects.get(url= 'index'),
            'Atendimentos': atendimento
        }
        return render(request, self.template, context)

    def post(self, request):
        cliente = Cliente.objects.get(cpf= request.POST.get('cpf') )
        atendimento = Atendimento() 
        atendimento.observacao = request.POST.get('obs')
        atendimento.data_solicitacao = request.POST.get('dataAtendimento')
        atendimento.cpf_cliente = cliente
        atendimento.save()
        context = {
            'menu': Menu.objects.get(url= 'visualizar_animal'),
            'Atendimentos': Atendimento.objects.all()
        }
        return render(request, self.template, context)

