from datetime import datetime
import json

from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.db.models import Sum, Count
from core.views import BaseView
from .models import (Animal, Cliente, Responsavel, Responde,
                     TipoStatusAnimal, StatusAnimal, TipoCliente, FichaAnimal)
from core.models import Menu
from cliente.exceptions import InvalidCPFError, DateError, MicrochipError
from cliente.actions import valida_cpf, valida_microchip, valida_cpf_responsavel
from servicos.models import Exame, FichaDiagnostico, DiagnosticoAnimal , TipoDiagnostico
from cloudinary_api.app import cloudyapi
from raven.contrib.django.raven_compat.models import client


from django.db import connection
from core.actions import dictfetchall


class ViewCadastrarCliente(BaseView):

    template = 'cadastro_cliente.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url='cadastro_cliente')
        }

        return render(request, self.template, context)

    def post(self, request):
        cliente = Cliente()

        try:
            cliente.cpf = request.POST.get('cpf')
            resposta = valida_cpf(cliente.cpf)

            if resposta['cpf'] is True:
                raise InvalidCPFError(resposta['msg'])

        except InvalidCPFError as e:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': str(e),
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.logradouro = request.POST.get('logradouro')
        cliente.bairro = request.POST.get('bairro')
        cliente.cidade = request.POST.get('cidade')
        cliente.estado = request.POST.get('estado')
        cliente.cep = request.POST.get('cep')
        cliente.numero = request.POST.get('numero')
        cliente.complemento = request.POST.get('complemento')

        tipo_cliente = request.POST.get('id_tipo_cliente')
        cliente.id_tipo_cliente = TipoCliente.objects.get(id=tipo_cliente)

        try:
            foto = request.FILES['url_foto']
        except Exception:
            foto = None

        if foto:
            foto = cloudyapi.upload_cliente_imagem(foto, cliente.pk)
            cliente.url_foto = foto['url']

        try:
            cliente.save()

        except Exception as e:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Ops! Não foi possível cadastrar este cliente',
                'time': 7000
            }

            return HttpResponse(json.dumps(context), content_type='application/json')

        context = {
            'tipo': 'ok',
            'mensagem': 'Cliente cadastrado com sucesso',
            'time': 5000
        }
        return HttpResponse(json.dumps(context), content_type='application/json')


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_animal.html'

    def get(self, request):
        context = {'menu': ''}

        if Menu.objects.get(url='cadastro_animal'):
            context['menu'] = Menu.objects.get(url='cadastro_animal')

        return render(request, self.template, context)

    def post(self, request):

        animal = Animal()
        context_responsavel = {}

        # Cliente
        try:
            cpf_cliente = request.POST.get('cpf_cliente')
            resposta = valida_cpf(cpf_cliente)

            if resposta['cpf'] is False:
                raise InvalidCPFError("Cliente inexistente")

            cliente = Cliente.objects.get(cpf=cpf_cliente)

        except InvalidCPFError as e:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': str(e),
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        # Animal
        try:
            datanasc = request.POST.get('datanasc')
            if datanasc is not '':
                animal.datanasc = datetime.strptime(datanasc, "%d/%m/%Y").strftime('%Y-%m-%d')

        except ValueError:
            raise DateError

        except DateError as e:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': str(e),
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        try:
            microchip = request.POST.get('microchip')
            resposta = valida_microchip(microchip)

            if resposta['microchip'] is True:
                raise MicrochipError(resposta['msg'])

            if microchip is not '':
                animal.microchip = microchip

        except MicrochipError as e:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': str(e),
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        animal.nome = request.POST.get('nome')
        animal.sexo = request.POST.get('sexo')
        animal.especie = request.POST.get('especie')
        animal.raca = request.POST.get('raca')
        animal.cor = request.POST.get('cor')
        animal.observacao = request.POST.get('observacao')
        animal.cpf_cliente = cliente

        try:
            animal.save()
        except Exception:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Ops! Não foi possível cadastrar este animal',
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        # Animal Foto
        try:
            arquivo = request.FILES['url_foto']
        except Exception:
            arquivo = None

        if arquivo is not None and animal.pk is not None:
            foto = cloudyapi.upload_animal_image(arquivo, animal.pk)
            animal.url_foto = foto['url']
            animal.save()

        context_animal = {
            'tipo': 'ok',
            'mensagem': 'Animal cadastrado com sucesso',
            'time': 7000
        }

        # Responsavel
        try:
            cpf_responsavel = request.POST.get('cpf_responsavel')
            responsavel = Responsavel.objects.get(cpf=cpf_responsavel)
            resposta_responsavel = valida_cpf_responsavel(cpf_responsavel)
        except:
            cpf_responsavel = request.POST.get('cpf_responsavel')
            responsavel = Responsavel()
            resposta_responsavel = valida_cpf_responsavel(cpf_responsavel)

        if cpf_responsavel != '' and resposta_responsavel['cpf'] is True:
            responde = Responde()
            responde.cpf_responsavel = responsavel
            responde.id_animal = animal
            responde.save()

            context_responsavel = {
                'tipo': 'informacao',
                'mensagem': "Animal associado ao responsável %s" % responsavel.nome,
                'time': 5000
            }

        if cpf_responsavel != '' and resposta_responsavel['cpf'] is False:
            try:
                responsavel.nome = request.POST.get('nome_responsavel')
                responsavel.cpf = cpf_responsavel
                responsavel.save()

                responde.cpf_responsavel = responsavel.cpf
                responde.id_animal = animal
                responde.save()

                context = {
                    'tipo': 'ok',
                    'mensagem': 'Responsável cadastrado com sucesso',
                    'time': 7000
                }
                context_responsavel = context
            except:
                client.captureException()
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Não foi possivel cadastrar o Responsável',
                    'time': 7000
                }
                context_responsavel = context

        # Status Animal
        # status_get = request.POST.get('status_animal')
        # Cadastra sempre um animal vivo
        status = TipoStatusAnimal.objects.get(nome='Vivo')

        status_animal = StatusAnimal()
        status_animal.id_status = status
        status_animal.id_animal = animal
        status_animal.save()

        context = {'dic_animal': context_animal,
                   'dic_responsavel': context_responsavel}

        return HttpResponse(json.dumps(context), content_type='application/json')


class ViewVisualizarAnimal(BaseView):

    template = 'visualizar_animal.html'

    def get(self, request):
        animal_list = Animal.objects.all()
        paginator = Paginator(animal_list, 10)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            animais = paginator.page(page)
        except (EmptyPage, InvalidPage):
            animais = paginator.page(paginator.num_pages)

        context = {
            'menu': Menu.objects.get(url='visualizar_animal'),
            'animal': animais
        }
        return render(request, self.template, context)

    def post(self, request):
        try:
            cpf_cliente = Cliente.objects.get(cpf=request.POST.get('cpf_cliente'))
            animal = Animal.objects.get(cpf_cliente=cpf_cliente, id=request.POST.get('id'))
            animal.nome = request.POST.get('nome')
            animal.sexo = request.POST.get('sexo')
            animal.especie = request.POST.get('especie')
            animal.raca = request.POST.get('raca')
            animal.cor = request.POST.get('cor')
            datanasc = request.POST.get('datanasc')
            animal.datanasc = datetime.strptime(datanasc, "%d/%m/%Y").strftime('%Y-%m-%d')
            animal.observacao = request.POST.get('obs')
            animal.microchip = request.POST.get('microchip')

            animal.cpf_cliente = cpf_cliente
            try:
                arquivo = request.FILES['url_foto']
            except Exception:
                arquivo = None

            if arquivo is not None and animal.pk is not None:
                foto = cloudyapi.upload_animal_image(arquivo, animal.pk)
                animal.url_foto = foto['url']

            animal.save()

            context = {
                'tipo': 'ok',
                'mensagem': 'Animal editado com sucesso',
                'time': 4000
            }

            return HttpResponse(json.dumps(context), content_type='application/json')

        except Exception:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Não foi possivel editar o animal',
                'time': 4000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

    def delete(self, request, id):
        animal = Animal.objects.get(pk=id)
        try:
            animal.delete()
            context = {
                'tipo': 'ok',
                'mensagem': 'Animal excluido com sucesso',
                'time': 4000
            }
        except IntegrityError:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Existe algum cliente associado a este animal',
                'time': 4000
            }

        return HttpResponse(json.dumps(context), content_type='application/json')


class ViewVisualizarCliente(BaseView):

    template = 'visualizar_cliente.html'

    def get(self, request):
        cliente_list = Cliente.objects.all()
        paginator = Paginator(cliente_list, 10)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            clientes = paginator.page(page)
        except (EmptyPage, InvalidPage):
            clientes = paginator.page(paginator.num_pages)

        context = {
            'menu': Menu.objects.get(url='visualizar_cliente'),
            'cliente': clientes
        }
        return render(request, self.template, context)

    def post(self, request):
        try:
            id = request.POST.get('id')
            cliente = Cliente.objects.get(pk=id)
            id_tipo_cliente = TipoCliente.objects.get(id=request.POST.get('id_tipo_cliente'))
            cliente.nome = request.POST.get('nome')
            cliente.cpf = request.POST.get('cpf')
            cliente.email = request.POST.get('email')
            cliente.cep = request.POST.get('cep')
            cliente.logradouro = request.POST.get('logradouro')
            cliente.numero = request.POST.get('numero')
            cliente.cidade = request.POST.get('cidade')
            cliente.bairro = request.POST.get('bairro')
            cliente.complemento = request.POST.get('complemento')
            cliente.id_tipo_cliente = id_tipo_cliente

            try:
                arquivo = request.FILES['url_foto']
            except Exception:
                arquivo = None

            if arquivo is not None and cliente.pk is not None:
                foto = cloudyapi.upload_cliente_imagem(arquivo, cliente.pk)
                cliente.url_foto = foto['url']

            try:
                cliente.save()
                context = {
                    'tipo': 'ok',
                    'mensagem': 'Cliente editado com sucesso',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            except:
                client.captureException()
                context = {
                    'tipo': 'erro',
                    'mensagem': 'Não foi possivel editar o cliente',
                    'time': 7000
                }
                return HttpResponse(json.dumps(context), content_type='application/json')
        except:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Não foi possivel editar o cliente',
                'time': 7000
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

    def delete(self, request, id):
        cliente = Cliente.objects.get(pk=id)
        try:
            cliente.delete()
            context = {
                'tipo': 'ok',
                'mensagem': 'Cliente excluido com sucesso',
                'time': 7000
            }
        except IntegrityError:
            client.captureException()
            context = {
                'tipo': 'erro',
                'mensagem': 'Ops...Existe algum animal associado a este cliente',
                'time': 4000
            }

        return HttpResponse(json.dumps(context), content_type='application/json')


class ViewFichaAnimal(BaseView):

    template = 'ficha_animal.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template, context)


class ViewBuscarAnimal(BaseView):
    templateficha = 'ficha_animal.html'
     
    def post(self, request):
        cliente = Cliente.objects.get(cpf=request.POST.get('cpf_cliente'))

        animal = Animal.objects.get(cpf_cliente=cliente, pk=request.POST.get('selectAnimal'))
        
        exames = Exame.objects.filter(id_animal=animal)

        query = """
            SELECT

                *

            FROM
                ATENDIMENTO AS ATEND
            INNER JOIN
                ATENDIMENTO_PROC_CLINICO AS ATE_CL ON (ATEND.id = ATE_CL.id_atendimento)
            INNER JOIN
                PROCEDIMENTO_CLINICO AS PC ON (PC.id = ATE_CL.id_proc_clinico)
                   
            WHERE
                ATEND.id_animal = {}
        """.format(animal.id)

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = dictfetchall(cursor)

        linhas= row

        context = {
            'cliente':cliente,  
            'animal': animal,
      
            'exames':exames,
            'historicos':linhas,
        }
        
        ficha = FichaAnimal.objects.filter( id_animal = animal.id).values(
            'id',
            'data_consulta',
            'descricao',
          
   
              )
        fichaGeral = FichaAnimal.objects.filter( id_animal = animal.id)

        fichadesc = FichaAnimal.objects.filter( id_animal = animal.id).values(
            'id',
            'fichadiagnostico_ficha__id_diagnostico__descricao',
   
              )



        query2 = """
             SELECT

                    *

             FROM
                    FICHA_ANIMAL AS FICHA
              left JOIN
                 FICHA_DIAGNOSTICO AS FICHA_DIAG ON (FICHA.id = FICHA_DIAG.id_ficha)
           INNER JOIN
                    DIAGNOSTICO_ANIMAL AS DIAG ON (FICHA_DIAG.id_diagnostico = DIAG.ID)   
                 
              WHERE
                 FICHA.id_animal = {} 
                   """.format(animal.id)

        with connection.cursor() as cursor:
            cursor.execute(query2)
            rowfICHA = dictfetchall(cursor)
 
        linhasFicha= rowfICHA
        novoDic = {}
 
        
        

      

        context['fichas'] = ficha
        context['fichasGerais'] = fichaGeral
        context['fichadesc'] = fichadesc

        return render(request, self.templateficha, context) 
    template = 'buscar_animal.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template, context)


class ViewAcompanheSuaClinica(BaseView):

    template = 'acompanhe_sua_clinica.html'

    def get(self, request):
        return render(request, self.template)
