from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from core.models import Menu, MenuGrupo

class ViewCadastroProcedimento(View):

    template = 'cadastro_procedimento.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.all().order_by('ordem'),
            'MenuGrupo': MenuGrupo.objects.all().order_by('ordem'),
            'menu_atual': Menu.objects.get(url= 'cadastro_procedimento')
        }
        return render(request, self.template, context)

class ViewCadastroEstadia(View):

    template = 'cadastro_estadia.html'

    def get(self, request):

        context = {
            'menu': Menu.objects.all().order_by('ordem'),
            'MenuGrupo': MenuGrupo.objects.all().order_by('ordem'),
            'menu_atual': Menu.objects.get(url= 'cadastro_estadia')
        }
        return render(request, self.template, context)


# Create your views here.
