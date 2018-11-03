from django.core import serializers
from django.http import HttpResponse


from .models import TipoCliente, Cliente, Animal, Responsavel


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

def get_animal(request, cpf_cliente, nome_animal):

    cliente = Cliente.objects.get(cpf=cpf_cliente)
    animal = Animal.objects.get(cpf_cliente=cliente, nome=nome_animal)

    data_json = serializers.serialize(
        "json", [cliente, animal], ensure_ascii=False
    )

    return HttpResponse(data_json, content_type='application/json')


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

