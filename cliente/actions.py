import json
import datetime 
from datetime import datetime, date
from django.core import serializers
from django.http import HttpResponse
from servicos.models import Atendimento ,FeitoPor
from usuarios.models import Funcionario
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
    
    data_sistema = datetime.strptime(data_init, "%Y-%m-%d").strftime('%d-%m-%Y')

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
            'mensagem':'Erro ao sincronizar informação com a google agenda',
            'time':5000       

              }       
    try:  
        atendimento.save()
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'Erro ao cadastrar atendimento',
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
            'mensagem':'Erro ao sincronizar Google Agenda',
            'time':5000       

              }       
    try:  
         feito = FeitoPor.objects.get(id_atendimento= id_evento)
         feito.delete()
     
    except Exception :
        context = {
            'tipo':"erro",
            'mensagem':'Erro ao excluir a informação de quem fez o procedimento',
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


def GravarAtendimento(request,dataAtendimento,hora_atendimento,obs,funcionarios,cpf_cliente,selectAnimal,radio):
    contador= 1
    periodo= 0
    if radio == 'M':
        contador = 5 
    if radio == 'S':
        contador = 4

    if radio == 'A':
        contador = 5

    if radio == 'N':
        contador = 1
               
    for cont in range(contador):

        var_data =  datetime.strptime(dataAtendimento, "%Y-%m-%d").strftime('%d-%m-%Y')
        data = dataAtendimento +'T'+hora_atendimento
        obssumary = request.POST.get('obs')

                #dicionario molde para o calendar
        event = {
            #-------------------------------CRIA O EVENTO--------------------------------
            'summary': obssumary,
            'location': 'Av. Dr. Alberto de Oliveira Lima, 254 - Real Parque, São Paulo',
            'description': obssumary,
                #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------
            'start': {
                'dateTime':  data+':00', # Adição da hora com o fusorario
                    'timeZone': 'America/Sao_Paulo',
                  },
                'end': {
                'dateTime':  data+':00',
                'timeZone': 'America/Sao_Paulo',
                #-------------------------------HORA QUE COMEÇA E TERMINA--------------------------------
                  },

                }

        data_nova = dataAtendimento
        hora_nova =hora_atendimento

        context = {
                'tipo':"ok",
                'mensagem':'Atendimento registrado',
                'time':5000,
                }
        try:
            google= GCalGoogle()
            gid = google.criar(event)
  
        except Exception :
            context = {
            'tipo':"erro",
            'mensagem':'Problema ao sincronzar com o google agenda',
            'time':5000,
             
              } 
            gid=''      
            return HttpResponse(json.dumps(context),content_type='application/json')  
        
        try:
            feito = FeitoPor()
            cliente = Cliente.objects.get(cpf= cpf_cliente )
            atendimento = Atendimento()
            atendimento.observacao = request.POST.get('obs') 
            data_nova =  datetime.strptime(dataAtendimento, "%Y-%m-%d").date()
            data_nova = date.fromordinal(data_nova.toordinal() + periodo) 
            data_nova = str(data_nova)
            data_atend = data_nova +' ' + hora_nova
            atendimento.data_solicitacao =  data_atend
            Atend_animal= Animal.objects.get(cpf_cliente=cliente, pk= selectAnimal)
            atendimento.id_animal = Atend_animal
            Responsavel = Funcionario.objects.get(cpf= funcionarios)
            atendimento.id_google_agenda = gid
            atendimento.save()
            feito.id_atendimento= atendimento
            feito.id_funcionario = Responsavel
            feito.save()
            context['id_data']= atendimento.id
            context['data_atend']= atendimento.data_solicitacao
            context['data_obs']= atendimento.observacao
            if radio == 'M':
                periodo = periodo + 30
            if radio == 'S':
                periodo = periodo + 7 
            if radio == 'A':
                periodo = periodo + 365
            if radio == 'N':
                periodo = 0       
        except Exception:   
        
            context = {
                'tipo':"erro",
                'mensagem':'Ocorreu um erro',
                'time':5000,

            }
            return HttpResponse(json.dumps(context),content_type='application/json')  
   
    return HttpResponse(json.dumps(context),content_type='application/json')          