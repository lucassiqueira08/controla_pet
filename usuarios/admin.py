from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from usuarios.models import (User, Funcionario, Veterinario,
                             Cargo, CargoFuncionario)
from usuarios.forms import (FormUser, FormAlteraUser, FormVeterinario,
                            FormFuncionario, FormAlteraFuncionario)

UserAuth = get_user_model()

class UsuarioAdmin(UserAdmin):

    form = FormAlteraUser
    fieldsets = ((None, {'fields': ('primeiro_nome',
                 'ultimo_nome', 'password')}),)
    add_form = FormUser
    add_fieldsets = ((None, {'fields': ('primeiro_nome', 'ultimo_nome')}),)
    list_display = ['login']
    filter_horizontal = []
    ordering = []
    list_filter = []


class FuncionarioAdmin(UserAdmin):

    form = FormAlteraFuncionario
    fieldsets = ((None, {'fields': (
        'primeiro_nome',
        'ultimo_nome',
        'cpf',
        'data_nasc',
        'equipe_sistema',
        'password',
    )}),)

    add_form = FormFuncionario
    add_fieldsets = ((None, {'fields': (
        'primeiro_nome',
        'ultimo_nome',
        'cpf',
        'data_nasc',
        'equipe_sistema'
    )}),)

    list_display = ['login']
    ordering = ['login']
    filter_horizontal = []
    list_filter = []


# admin.site.register(UserAuth)
admin.site.register(User, UsuarioAdmin)
# admin.site.register(Funcionario)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Veterinario)
admin.site.register(Cargo)
admin.site.register(CargoFuncionario)
