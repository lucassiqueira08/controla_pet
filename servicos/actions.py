import json
import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.core import serializers

from servicos.models import (ProcedimentoEstetico, ProcedimentoClinico,
                             TipoProcedimento, StatusEstadia, StatusAtendimento,
                             AtendimentoProcClinico)

def get_tipo_procedimento(request):
    tipo_procedimento        = TipoProcedimento.objects.all()
    tipo_procedimento_json   = serializers.serialize("json", tipo_procedimento)
    return HttpResponse(tipo_procedimento_json, content_type='application/json')


def get_procedimento(request):
    procedimento_clinico  = ProcedimentoClinico.objects.all()
    procedimento_estetico = ProcedimentoEstetico.objects.all()

    all_objects = list(ProcedimentoClinico.objects.all()) + list(
        ProcedimentoEstetico.objects.all()
    )

    data_json = serializers.serialize(
        "json", all_objects
    )
    return HttpResponse(data_json, content_type='application/json')


def get_animais_hospedados(request):
    estadia = StatusEstadia.objects.filter(id_status__nome_status='aberto',).values(
        'id_estadia__id_animal__nome',
        'id_estadia__data_inicio',
        'id_estadia__data_fim',
        'id_status__nome_status'
    )
    context = []

    for item in estadia:
        context.append(item)

    data = json.dumps(context, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def get_atendimentos_pendentes(request):
    atendimento = StatusAtendimento.objects.exclude(id_status__nome='fechado').filter(
        id_atendimento__feitopor_atendimento__data_realizacao__gte=datetime.date.today()
    ).values(
        'id_atendimento__id_cliente__nome',
        'id_atendimento__feitopor_atendimento__data_realizacao',
        'id_status__nome',
    )
    context = []

    for item in atendimento:
        context.append(item)

    data = json.dumps(context, sort_keys=True, indent=1, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type='application/json')


def get_pagamentos_pendentes(request):
    pagamento_pendente = StatusAtendimento.objects.filter(id_status__nome='aguardando pagamento').values(
        'id_atendimento__id_cliente__id_tipo_cliente__nome',
        'id_atendimento__id_cliente__nome',
        'id_atendimento__id_orcamento__preco_final',
        'id_atendimento__feitopor_atendimento__data_realizacao',
        'id_status__nome',
    )
    context = []

    for item in pagamento_pendente:
        context.append(item)

    data = json.dumps(context, sort_keys=True, indent=1, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type='application/json')
