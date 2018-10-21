from django.http import HttpResponse
from django.core import serializers

from .models import TipoCliente, Cliente
from .exceptions import InvalidCPFError

def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')


def valida_cpf(cpf):
    cliente = Cliente.objects.filter(cpf=cpf)
    if cliente:
        return {'error': True, 'msg': 'CPF já cadastrado'}

    return {'error': False}
