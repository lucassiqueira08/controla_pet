from django.shortcuts import render

from core.views import BaseView
from .forms import FormCliente
from .models import Animal, Cliente


class ViewCadastrarCliente(BaseView):

    template = 'cadastro_cliente.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = FormCliente(request.POST)
        if form.is_valid:
            form.save()
        return render(request, self.template)


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_animal.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        cpf_cliente = request.POST.get('cpf_cliente')
        cliente = Cliente.objects.get(cpf=cpf_cliente)
        animal = Animal()
        animal.nome = request.POST.get('nome')
        animal.sexo = request.POST.get('sexo')
        animal.especie = request.POST.get('especie')
        animal.raca = request.POST.get('raca')
        animal.cor = request.POST.get('cor')
        animal.datanasc = '1997-11-24'
        animal.observacao = request.POST.get('observacao')
        animal.microchip = request.POST.get('microchip')
        animal.cpf_cliente = cliente
        animal.save()
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        return render(request, self.template)
