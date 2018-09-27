from django.http import HttpResponse
from django.core import serializers

from .models import TipoCliente


def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')
