from django.core import serializers
from django.http import HttpResponse

from .models import TipoCliente, Animal, Cliente


def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')


def get_animal(request, cpf_cliente, nome_animal):

    cliente = Cliente.objects.get(cpf=cpf_cliente)
    animal = Animal.objects.get(cpf_cliente=cliente, nome=nome_animal)

    data_json = serializers.serialize(
        "json", [cliente, animal], ensure_ascii=False
    )

    return HttpResponse(data_json, content_type='application/json')
