from django.http import HttpResponse
from django.core import serializers

from .models import TipoCliente , Cliente , Animal


def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')


def get_ficha_animal(request, cpf_cliente , nome_animal):
    cliente = Cliente.objects.get(pk=cpf_cliente)
    animal= Animal.objects.get(nome=nome_animal,cpf_cliente=cliente)
    data = ([animal,cliente])
    cliente_json = serializers.serialize("json", data)
    return HttpResponse(cliente_json, content_type='application/json')
