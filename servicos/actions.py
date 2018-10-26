from django.http import HttpResponse
from django.core import serializers

from servicos.models import TipoProcedimento

def get_tipo_procedimento(request):
    tipo_procedimento        = TipoProcedimento.objects.all()
    tipo_procedimento_json   = serializers.serialize("json", tipo_procedimento)
    return HttpResponse(tipo_procedimento_json, content_type='application/json')
