import json
import datetime 
from django.core import serializers
from django.http import HttpResponse
from servicos.models import Atendimento ,FeitoPor
from gagenda.app import GCalGoogle

from .models import TipoCliente, Cliente, Animal, Responsavel


def get_cliente(request):
    cliente = TipoCliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')


def get_animal(request, cpf_cliente, nome_animal):

    cliente = Cliente.objects.get(cpf=cpf_cliente)
    animal = Animal.objects.get(cpf_cliente=cliente, nome=nome_animal)

    data_json = serializers.serialize(
        "json", [cliente, animal], ensure_ascii=False
    )

    return HttpResponse(data_json, content_type='application/json')


def get_ficha_animal(request, cpf_cliente , id_animal):

    cliente = Cliente.objects.filter(cpf=cpf_cliente).first()
    if cliente:
        animal= Animal.objects.filter(pk=id_animal,cpf_cliente=cliente).first()
        if animal:
            data = ([animal,cliente])
            cliente_json = serializers.serialize("json", data)
            return HttpResponse(cliente_json, content_type='application/json')

        context = {
            'tipo':"erro",
            'mensagem':"Não foi encontrado um animal para este CPF",
            'time':5000
        }
        return HttpResponse(json.dumps(context),content_type='application/json')
    context = {
        'tipo':"erro",
        'mensagem':"Este cliente não foi cadastrado ou o cpf esta incorreto",
        'time':5000
    }
    return HttpResponse(json.dumps(context),content_type='application/json')


def valida_cpf(cpf):
    cliente = Cliente.objects.filter(cpf=cpf)
    if cliente:
        return {'cpf': True, 'msg': 'CPF já cadastrado'}
    return {'cpf': False}


def valida_microchip(microchip):
    animal = Animal.objects.filter(microchip=microchip)
    if animal and microchip is not '':
        return {'microchip': True, 'msg': 'Microchip já cadastrado'}
    return {'microchip': False}


def valida_cpf_responsavel(cpf):
    responsavel = Responsavel.objects.filter(cpf=cpf)
    if responsavel:
        return {'cpf': True, 'msg': 'Responsável já cadastrado'}
    return {'cpf': False}


def get_cliente_id(request):
    id = request.POST.get('cpf_cliente')
    if id:
        cliente = Cliente.objects.filter(id=id)
    else:
        cliente = Cliente.objects.all()
    cliente_json = serializers.serialize("json", cliente)
    return HttpResponse(cliente_json, content_type='application/json')

def get_atualiza_atendimento(request,id_evento,observacao,data_init,horaedit):
    atendimento = Atendimento.objects.get(id = id_evento)
    atendimento.observacao = observacao
    
    data_sistema = datetime.datetime.strptime(data_init, "%Y-%m-%d").strftime('%d-%m-%Y')

    data = data_init+'T'+horaedit+':00-03:00'

    atendimento.data_solicitacao = data_init + ' '+ horaedit 

    google= GCalGoogle()
    IdGoogle = atendimento.id_google_agenda

    coment = observacao
    try:
        google.atualizar(IdGoogle,coment,data,data)
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'erro google'+data,
            'time':5000       

              }       
    try:  
        atendimento.save()
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'erro atendi' + data_init,
            'time':5000       

              }   

    context = {
            'tipo':"ok",
            'mensagem':'Data atualizada com sucesso ',
            'time':5000       

              }       
   
    return HttpResponse(json.dumps(context),content_type='application/json')


def get_deleta_atendimento(request,id_evento):

    try:
        atendimento = Atendimento.objects.get(id = id_evento)
        google= GCalGoogle()
        google.deletar(atendimento.id_google_agenda)
        
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'erro google'+data,
            'time':5000       

              }       
    try:  
         feito = FeitoPor.objects.get(id_atendimento= id_evento)
         feito.delete()
     
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'Erro ao excluir a informação de quem fez',
            'time':5000       

              }   
    try:  
        atendimento.delete()
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'Erro ao excluir atendimento',
            'time':5000       

              }   
              
    context = {
            'tipo':"ok",
            'mensagem':'Atendimento excluido',
            'time':5000       

              }       
   
    return HttpResponse(json.dumps(context),content_type='application/json')  







