from django.shortcuts import render

from core.views import BaseView

class ViewCadastrarCliente(BaseView):

    template = 'cadastro_cliente.html'

    def get(self, request):
        return render(request, self.template)


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_animal.html'

    def get(self, request):
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        return render(request, self.template)
