from django.core import serializers
from django.http import HttpResponse

from .models import (ProcedimentoEstetico, ProcedimentoClinico)


def get_procedimento(request):
    procedimento_clinico = ProcedimentoClinico.objects.all()
    procedimento_estetico = ProcedimentoEstetico.objects.all()

    all_objects = list(ProcedimentoClinico.objects.all()) + list(ProcedimentoEstetico.objects.all())

    data_json = serializers.serialize(
        "json", all_objects
    )
    return HttpResponse(data_json, content_type='application/json')
