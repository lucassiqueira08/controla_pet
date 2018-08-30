from django.shortcuts import render

from core.views import BaseView
from .forms import FormAnimal, FormCliente


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
        form = FormAnimal(request.POST)
        if form.is_valid:
            form.save()
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        return render(request, self.template)
