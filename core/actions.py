
import datetime

from django.http import HttpResponse
from django.core import serializers

from servicos.models import Atendimento, FeitoPor, AtendimentoProcClinico, AtendimentoProcEstetico, StatusAtendimento



def get_Atendimentos(request):
    atendimento = Atendimento.objects.all()
    atendimento_json = serializers.serialize("json", atendimento)
    return HttpResponse(atendimento_json, content_type='application/json')


def get_notificacao(request):
    atendimentos = Atendimento.objects.prefetch_related((data_solicitacao__contains='2018-10').only('comissao'))
    atendimento_json = serializers.serialize("json", atendimentos)
    response = []
    for atendimento in atendimentos:
        feito_por = FeitoPor.objects.filter(id_atendimento=atendimento.pk)
        feito_por_json = serializers.serialize("json", feito_por)
        response.append(feito_por_json)


    # func = FeitoPor.objects.filter(id_atendimento=atendimento)
    # func_json = serializers.serialize("json", func)

    # proc_clinico = AtendimentoProcClinico.objects.all()
    # proc_estetico = AtendimentoProcEstetico.objects.all()
    # status = StatusAtendimento.objects.all()

    return HttpResponse(atendimento_json, content_type='application/json')
