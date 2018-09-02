from datetime import datetime
from pprint import pprint

from django.shortcuts import render

from core.views import BaseView
from .forms import FormCliente
from .models import (Animal, Cliente, Responsavel, Responde,
                     TipoStatusAnimal, StatusAnimal)
from core.models import Menu


class ViewCadastrarCliente(BaseView):

    template = 'cadastro_cliente.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'cadastro_estadia')
        }
        return render(request, self.template, context)

    def post(self, request):
        form = FormCliente(request.POST)
        if form.is_valid:
            form.save()
        return render(request, self.template)


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_animal.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'cadastro_estadia')
        }
        return render(request, self.template, context)

    def post(self, request):
        cpf_cliente = request.POST.get('cpf_cliente')
        cliente = Cliente.objects.get(cpf=cpf_cliente)

        cpf_responsavel = request.POST.get('cpf_responsavel')

        try:
            responsavel = Responsavel.objects.get(cpf=cpf_responsavel)
        except Exception:
            responsavel = Responsavel()
            responsavel.nome = request.POST.get('nome_responsavel')
            responsavel.cpf = cpf_responsavel
            responsavel.save()

        datanasc = request.POST.get('datanasc')
        animal = Animal()
        animal.nome = request.POST.get('especie')
        animal.sexo = request.POST.get('sexo')
        animal.especie = request.POST.get('especie')
        animal.raca = request.POST.get('raca')
        animal.cor = request.POST.get('cor')
        animal.datanasc = datetime.strptime(datanasc, "%d/%m/%Y").strftime('%Y-%m-%d')
        animal.observacao = request.POST.get('observacao')
        animal.microchip = request.POST.get('microchip')
        animal.cpf_cliente = cliente
        animal.save()

        responde = Responde()
        responde.cpf_responsavel = responsavel
        responde.id_animal = animal
        responde.save()

        status_get = request.POST.get('status_animal')
        status = TipoStatusAnimal.objects.get(nome=status_get)

        status_animal = StatusAnimal()
        status_animal.id_status = status
        status_animal.id_animal = animal
        status_animal.save()
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'visualizar_animal')
        }
        return render(request, self.template, context)

class ViewFichaAnimal(BaseView):

    template = 'ficha_animal.html'

    def get(self, request):
        return render(request, self.template)