from django.http import HttpResponse
from django.core import serializers

from servicos.models import Atendimento


def get_Atendimentos(request):
    atendimento = Atendimento.objects.all()
    atendimento_json = serializers.serialize("json", atendimento)
    return HttpResponse(atendimento_json, content_type='application/json')
