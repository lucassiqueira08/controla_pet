from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from core.models import Menu


class ViewCadastroServico(View):

    template = 'cadastro_servico.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'cadastro_servico')
        }
        return render(request, self.template, context)

class ViewCadastroEstadia(View):

    template = 'cadastro_estadia.html'

    def get(self, request):

        context = {
            'menu': Menu.objects.get(url= 'cadastro_estadia')
        }
        return render(request, self.template, context)


# Create your views here.
