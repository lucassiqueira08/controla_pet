import json

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import render
from django.views import View

from django.http import HttpResponse

from core.models import Menu
from servicos.models import ProcedimentoClinico,ProcedimentoEstetico, TipoProcedimento


class ViewCadastroProcedimento(View):

    template = 'cadastro_procedimento.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template, context)

    def post(self, request):
        nome                  = request.POST.get('nome')
        descricao             = request.POST.get('descricao')
        preco                 = request.POST.get('preco')
        especie               = request.POST.get('especie')
        aba_procedimento      = request.POST.get('aba_procedimento')


        print('******************************')
        print(aba_procedimento)

        if aba_procedimento == 'clinico':
            tipo_procedimento = request.POST.get('tipo_procedimento')

            procedimento              = ProcedimentoClinico()
            procedimento.nome         = nome
            procedimento.descricao    = descricao
            procedimento.preco        = preco.replace(",",".")
            procedimento.especie      = especie
            procedimento.id_tipo_proc = TipoProcedimento.objects.get(id=tipo_procedimento)
            procedimento.save()
        if aba_procedimento == 'estetico':
            procedimento            = ProcedimentoEstetico()
            procedimento.nome       = nome
            procedimento.descricao  = descricao
            procedimento.preco      = preco.replace(",",".")
            procedimento.especie    = especie
            procedimento.save()
        context = {'menu': ''}

        try:
            context['menu'] = Menu.objects.get(url='cadastro_animal')

        except ObjectDoesNotExist:
            context['menu'] = Menu.objects.get(url='index')

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
            'menu': Menu.objects.get(url= 'cadastro_estadia')
        }
        return render(request, self.template, context)


class ViewModal(View):

    template = 'modal_orcamento.html'

    def get(self, request):
        return render(request, self.template)

class ViewCadastroAtendimento(View):

    template = 'cadastro_atendimento.html'

    def get(self, request):
        return render(request, self.template)


# Create your views here.
