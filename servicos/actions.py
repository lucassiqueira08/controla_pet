import json

from django.http import HttpResponse
from django.core import serializers

from servicos.models import TipoProcedimento, DiagnosticoAnimal, TipoDiagnostico, TipoExame
from cliente.models import Cliente
from cliente.models import Animal


def get_tipo_procedimento(request):
    tipo_procedimento = TipoProcedimento.objects.all()
    tipo_procedimento_json = serializers.serialize("json", tipo_procedimento)
    return HttpResponse(tipo_procedimento_json, content_type='application/json')


def get_animais_cliente(request):
    cpf_cliente = request.GET.get('cpf_cliente')
    cliente = Cliente.objects.filter(cpf=cpf_cliente).first()
    animais_cliente = Animal.objects.filter(cpf_cliente=cliente)
    animais_cliente_json = serializers.serialize("json", animais_cliente)
    return HttpResponse(animais_cliente_json, content_type='application/json')


def get_animal(request):
    cpf_cliente = request.GET.get('cpf_cliente')
    id_animal = request.GET.get('id_animal')
    animal = Animal.objects.filter(pk=id_animal)
    cliente = Cliente.objects.filter(cpf=cpf_cliente)
    animal_json = serializers.serialize("json", animal)
    return HttpResponse(animal_json, content_type='application/json')


def get_diagnostico(request):
    tipos_diagnostico = TipoDiagnostico.objects.all().values()
    response = []
    for tipo in tipos_diagnostico:
        dic = {}
        dic['tipo'] = tipo
        dic['diagnosticos'] = list(DiagnosticoAnimal.objects.filter(
            id_tipo_diagnostico=tipo['id']).values('id', 'descricao'))
        response.append(dic)
    return HttpResponse(json.dumps(response), content_type='application/json')


def get_tipo_exame(request):
    tipo_exame = TipoExame.objects.all()
    tipo_exame_json = serializers.serialize("json", tipo_exame)
    return HttpResponse(tipo_exame_json, content_type='application/json')
