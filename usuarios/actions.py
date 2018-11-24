from django.core import serializers
from django.http import HttpResponse

from .models import User, Cargo


def get_funcionario(request):
    funcionario = User.objects.filter(funcionario__isnull=False)
    funcionario_json = serializers.serialize(
        "json", funcionario, fields=('pk', 'primeiro_nome', 'ultimo_nome')
    )
    return HttpResponse(funcionario_json, content_type='application/json')

def get_cargo(request):
    cargos = Cargo.objects.all()
    cargos_json = serializers.serialize("json", cargos)
    return HttpResponse(cargos_json, content_type='application/json')
