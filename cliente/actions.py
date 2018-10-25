from django.core import serializers
from django.http import HttpResponse


from .models import TipoCliente, Cliente, Animal, Responsavel


def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')


def valida_cpf(cpf):
    cliente = Cliente.objects.filter(cpf=cpf)
    if cliente:
        return {'cpf': True, 'msg': 'CPF já cadastrado'}
    return {'cpf': False}


def valida_microchip(microchip):
    animal = Animal.objects.filter(microchip=microchip)
    if animal:
        return {'microchip': True, 'msg': 'Microchip já cadastrado'}
    return {'microchip': False}


def valida_cpf_responsavel(cpf):
    responsavel = Responsavel.objects.filter(cpf=cpf)
    if responsavel:
        return {'cpf': True, 'msg': 'Responsável já cadastrado'}
    return {'cpf': False}

