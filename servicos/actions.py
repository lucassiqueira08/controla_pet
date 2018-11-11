from django.http import HttpResponse
from django.core import serializers

from servicos.models import TipoProcedimento
from cliente.models import Cliente
from cliente.models import Animal

def get_tipo_procedimento(request):
    tipo_procedimento        = TipoProcedimento.objects.all()
    tipo_procedimento_json   = serializers.serialize("json", tipo_procedimento)
    return HttpResponse(tipo_procedimento_json, content_type='application/json')

def get_animais_cliente(request):
    print("********************************")

    cpf_cliente           = request.GET.get('cpf_cliente')
    cliente               = Cliente.objects.filter(cpf = cpf_cliente).first()
    animais_cliente       = Animal.objects.filter(cpf_cliente = cliente)
    animais_cliente_json  = serializers.serialize("json", animais_cliente)
    print(animais_cliente_json)
    return HttpResponse(animais_cliente_json, content_type='application/json')
