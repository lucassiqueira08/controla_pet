
import datetime
import json

from django.http import HttpResponse
from django.db import connection
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from servicos.models import Atendimento


def get_atendimentos(request):
    atendimento = Atendimento.objects.all()
    atendimento_json = serializers.serialize("json", atendimento)
    return HttpResponse(atendimento_json, content_type='application/json')


def dictfetchall(cursor):
    """
        Retorna todas as linhas do cursor como um dicionario
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_notificacao(request):
    """
    Função que retorna dados para a que a notificação seja exibida no frontend

    param: request
    return: json
    """
    date_now = datetime.datetime.now()
    year = date_now.strftime("%Y")
    month = date_now.strftime("%m")
    query_date = year + '-' + month

    try:
        notificacao = Atendimento.objects.filter(data_solicitacao__month=month,
                                                 data_solicitacao__year=year).values(
            'id',
            'statusatendimento_atendimento__id_status__nome',
            'data_solicitacao',
            'id_animal__especie',
            'atendimentoprocestetico_atendimento__id_proc_estetico__nome',
            'atendimentoprocclinico_atendimento__id_proc_clinico__nome',
            'id_animal__cpf_cliente__nome',
            'id_animal__cpf_cliente__cpf',
            'feitopor_atendimento__id_funcionario__primeiro_nome',
        )

        context = json.dumps(
            list(notificacao),
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )

    except Exception:
        context = {}

    return HttpResponse(json.dumps(context), content_type='application/json')
