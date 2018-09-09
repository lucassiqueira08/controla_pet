from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from .models import Menu, MenuGrupo


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
        context = {
            'menu': Menu.objects.get(url= 'index')
        }
        return render(request, self.template, context)

