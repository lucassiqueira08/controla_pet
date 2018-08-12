from django.shortcuts import render
from django.views import View


class ViewEsqueceuSenha(View):

    template = 'esqueceu_senha.html'

    def get(self, request):
        return render(request, self.template)
