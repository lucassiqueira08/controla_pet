from django.core import serializers
from django.http import HttpResponse

from .models import User


def get_funcionario(request):
    funcionario = User.objects.filter(funcionario__isnull=False)
    funcionario_json = serializers.serialize(
        "json", funcionario, fields=('pk', 'primeiro_nome', 'ultimo_nome')
    )
    return HttpResponse(funcionario_json, content_type='application/json')
