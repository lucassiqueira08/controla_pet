from datetime import datetime
from pprint import pprint

from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.files.uploadedfile import UploadedFile, TemporaryUploadedFile

from core.views import BaseView
from .forms import FormCliente
from .models import (Animal, Cliente, Responsavel, Responde,
                     TipoStatusAnimal, StatusAnimal)
from core.models import Menu
from gdstorage.app import upload_animal_images


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
        arquivo = request.FILES['url_foto']

        temp_arquivo = TemporaryUploadedFile(name=arquivo.name,
                                             content_type=arquivo.content_type,
                                             size=arquivo.size,
                                             charset=arquivo.charset)

        temp_path = temp_arquivo.temporary_file_path()

        destination = open(temp_path, 'wb+')
        for chunk in arquivo.chunks():
            destination.write(chunk)
        destination.close()

        animal.url_foto = upload_animal_images(animal.pk, temp_path)

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
            'menu': Menu.objects.get(url= 'ficha_animal')
        }
        return render(request, self.template, context)
class ViewAcompanheSuaClinica(BaseView):

    template = 'acompanhe_sua_clinica.html'

    def get(self, request):
        return render(request, self.template)
