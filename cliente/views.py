from django.shortcuts import render

from core.views import BaseView
from .forms import FormAnimal, FormCliente
from .models import Animal, TipoStatusAnimal, StatusAnimal


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
        cpf_cliente = request.POST.get('cpf_cliente','')
        nome = request.POST.get('nome', '')
        sexo = request.POST.get('sexo', '')
        especie = request.POST.get('especie', '')
        raca = request.POST.get('raca', '')
        cor = request.POST.get('cor', '')
        observacao = request.POST.get('observacao', '')
        microchip = request.POST.get('microchip', '')
        animal = Animal(nome=nome, sexo=sexo, especie=especie, raca=raca, cor=cor, observacao=observacao, microchip=microchip, cpf_cliente=cpf_cliente)
        animal.save()
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        return render(request, self.template)
