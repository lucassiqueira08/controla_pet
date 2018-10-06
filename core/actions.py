
import datetime
import json

from django.http import HttpResponse
from django.db import connection
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from servicos.models import Atendimento, FeitoPor, AtendimentoProcClinico, AtendimentoProcEstetico, StatusAtendimento


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

    TODO: Melhorar a função para que não abra conexão com o banco de dados diretamente, e sim utilize o Django ORM
    """
    date_now = datetime.datetime.now()
    year = date_now.strftime("%Y")
    month = date_now.strftime("%m")
    query_date = year + '-' + month

    try:
        query = """
            SELECT
                ATE.id AS id,
                TSA.nome AS status_atendimento,
                ATE.data_solicitacao AS 'data/hora',
                PE.especie AS especie,
                PE.nome AS procedimento_estetico,
                PC.nome AS procedimento_clinico,
                CLI.nome AS dono,
                CLI.cpf AS cpf_cliente,
                U.primeiro_nome AS responsavel
            FROM
                ATENDIMENTO AS ATE
                    LEFT JOIN
                ATENDIMENTO_PROC_ESTETICO AS ATE_PE ON (ATE.id = ATE_PE.id_atendimento)
                    LEFT JOIN
                PROCEDIMENTO_ESTETICO AS PE ON (PE.id = ATE_PE.id_proc_estetico)
                    LEFT JOIN
                CLIENTE AS CLI ON (ATE.cpf_cliente = CLI.cpf)
                    LEFT JOIN
                ATENDIMENTO_PROC_CLINICO AS ATE_CL ON (ATE.id = ATE_CL.id_atendimento)
                    LEFT JOIN
                PROCEDIMENTO_CLINICO AS PC ON (PC.id = ATE_CL.id_proc_clinico)
                    LEFT JOIN
                FEITO_POR AS FP ON (FP.id_atendimento = ATE.id)
                    LEFT JOIN
                FUNCIONARIO AS FUN ON (FUN.user_ptr_id = FP.id_funcionario)
                    LEFT JOIN
                USER AS U ON (U.id = FUN.user_ptr_id)
                    LEFT JOIN
                STATUS_ATENDIMENTO AS ST ON (ATE.id = ST.id_atendimento)
                    LEFT JOIN
                TIPO_STATUS_ATENDIMENTO AS TSA ON (TSA.id = ST.id_status);
            WHERE
                ATE.data_solicitacao = %s
        """ % query_date

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = dictfetchall(cursor)

        atendimentos = row

        context = json.dumps(
            atendimentos,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )

    except Exception:
        context = {}

    return HttpResponse(json.dumps(context), content_type='application/json')
