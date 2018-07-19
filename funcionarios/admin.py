from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from funcionarios.forms import (FormVeterinario, FormFuncionario, FormAlteraFuncionario)
from funcionarios.models import Funcionario, Veterinario


class FuncionarioAdmin(UserAdmin):

    form = FormAlteraFuncionario
    fieldsets = ((None, {'fields': ('primeiro_nome', 'ultimo_nome', 'cpf', 'data_nasc', 'equipe_sistema', 'password')}),)
    add_form = FormFuncionario
    add_fieldsets = ((None, {'fields': ('primeiro_nome', 'ultimo_nome', 'cpf', 'data_nasc', 'equipe_sistema')}),)
    list_display = ['login']
    ordering = ['login']
    filter_horizontal = []
    list_filter = []


# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Veterinario)
