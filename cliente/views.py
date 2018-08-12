from django.shortcuts import render

from core.views import BaseView


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_de_animal.html'

    def get(self, request):
        return render(request, self.template)


class ViewVisualizacaoAnimal(BaseView):

    template = 'visualizacao_animal.html'

    def get(self, request):
        return render(request, self.template)
