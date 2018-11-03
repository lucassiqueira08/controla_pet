from datetime import datetime
from pprint import pprint

from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.files.uploadedfile import UploadedFile, TemporaryUploadedFile

from core.views import BaseView
from .forms import FormCliente
from servicos.models import Exame , Atendimento , AtendimentoProcClinico , ProcedimentoClinico
from .models import (Animal, Cliente, Responsavel, Responde,
                     TipoStatusAnimal, StatusAnimal, FichaAnimal)
from core.models import Menu
from django.db import connection
from core.actions import dictfetchall
import json

from django.core.serializers.json import DjangoJSONEncoder

from cloudinary_api.app import cloudyapi



class ViewCadastrarCliente(BaseView):

    template = 'cadastro_cliente.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'cadastro_cliente')
        }
        return render(request, self.template, context)

    def post(self, request):
        form = FormCliente(request.POST)
        if form.is_valid:
            form.save()
        return render(request, self.template)


class ViewCadastrarAnimal(BaseView):

    template = 'cadastro_animal.html'

    def get(self, request):
        context = {
            'menu': Menu.objects.get(url= 'cadastro_animal')
        }
        return render(request, self.template, context)

    def post(self, request):
        cpf_cliente = request.POST.get('cpf_cliente')
        cliente = Cliente.objects.get(cpf=cpf_cliente)

        cpf_responsavel = request.POST.get('cpf_responsavel')

        try:
            responsavel = Responsavel.objects.get(cpf=cpf_responsavel)
        except Exception:
            responsavel = Responsavel()
            responsavel.nome = request.POST.get('nome_responsavel')
            responsavel.cpf = cpf_responsavel
            responsavel.save()

        datanasc = request.POST.get('datanasc')
        animal = Animal()
        animal.nome = request.POST.get('especie')
        animal.sexo = request.POST.get('sexo')
        animal.especie = request.POST.get('especie')
        animal.raca = request.POST.get('raca')
        animal.cor = request.POST.get('cor')
        animal.datanasc = datetime.strptime(datanasc, "%d/%m/%Y").strftime('%Y-%m-%d')
        animal.observacao = request.POST.get('observacao')
        animal.microchip = request.POST.get('microchip')
        animal.cpf_cliente = cliente
        animal.save()

        responde = Responde()
        responde.cpf_responsavel = responsavel
        responde.id_animal = animal
        responde.save()

        status_get = request.POST.get('status_animal')
        status = TipoStatusAnimal.objects.get(nome=status_get)

        status_animal = StatusAnimal()
        status_animal.id_status = status
        status_animal.id_animal = animal
        status_animal.save()
        return render(request, self.template)


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
            'menu': Menu.objects.get(url= 'visualizar_animal'),
            'animal': animais
        }
        return render(request, self.template, context)

    def post(self, request):
        cpf_cliente = Cliente.objects.get(cpf=request.POST.get('cpf_cliente'))
        animal = Animal.objects.get(cpf_cliente=cpf_cliente, microchip=request.POST.get('microchip'))
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

        if request.POST.get('button') == 'del':
            animal.delete()
        if request.POST.get('button') == 'save':
            animal.save()

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
            'menu': Menu.objects.get(url= 'visualizar_animal'),
            'animal': animais
        }
        return render(request, self.template, context)


class ViewFichaAnimal(BaseView):

    template = 'ficha_animal.html'  
 

    def get(self, request):
        context = {   
        }
        return render(request, self.template, context)

class ViewCadastrarDiagnostico(BaseView):

    template = 'cadastrar_diagnostico.html'

    def get(self, request):
        context = {


        }
        return render(request, self.template, context)

class ViewBuscarAnimal(BaseView):
    templateficha = 'ficha_animal.html'
     


    def post(self, request):
        cliente = Cliente.objects.get(cpf=request.POST.get('cpf_cliente'))
        animal = Animal.objects.get(cpf_cliente=cliente, nome=request.POST.get('nome_animal'))
        ficha = FichaAnimal.objects.get(id_animal=animal)
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
                ATEND.id_animal = '1'
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = dictfetchall(cursor)

        linhas= row

        historicos = json.dumps(
             linhas,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )

        context = {
            'cliente':cliente,  
            'animal': animal,
            'ficha':ficha,
            'exames':exames,
            'historicos':linhas,
        }
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
