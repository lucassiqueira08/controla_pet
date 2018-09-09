from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from core.models import Menu


class ViewCadastroProcedimento(View):

    template = 'cadastro_procedimento.html'

    def get(self, request):
        return render(request, self.template)

class ViewCadastroEstadia(View):

    template = 'cadastro_estadia.html'

    def get(self, request):
        return render(request, self.template)


# Create your views here.
