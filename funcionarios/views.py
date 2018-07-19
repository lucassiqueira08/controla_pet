from django.shortcuts import render
from django.http import request

from funcionarios.forms import FormFuncionario, FormVeterinario


def view_cadastrar_funcionario(request):

    if request.POST:
        form = FormFuncionario(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = FormFuncionario()

    contexto = {'form': form}
    pass
    #return render(request, "cadastrar_funcionario.html", contexto)


def view_cadastrar_veterinario(request):

    if request.POST:
        form = FormVeterinario(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = FormVeterinario()

    contexto = {'form': form}
    pass


# Create your views here.
