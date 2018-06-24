from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuarios.models import User
from usuarios.forms import FormUser, FormAlteraUser


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


admin.site.register(User, UsuarioAdmin)
# Register your models here.
