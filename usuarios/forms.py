from django import forms

from usuarios.models import User, Funcionario, Veterinario


class FormUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['primeiro_nome', 'ultimo_nome']

    def save(self, commit=True):
        usuario = super(FormUser, self).save(commit=False)
        usuario.set_password("123@mudar")
        if commit:
            usuario.save()
        return usuario


class FormAlteraUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['primeiro_nome', 'ultimo_nome', 'password']


class FormFuncionario(forms.ModelForm):

    def save(self, commit=True):
        usuario = super(FormFuncionario, self).save(commit=False)
        usuario.set_password("123@mudar")
        if commit:
            usuario.save()
        return usuario

    class Meta:
        model = Funcionario
        fields = [
            'primeiro_nome',
            'ultimo_nome',
            'apelido',
            'situacao_func',
            'cpf',
            'data_nasc',
            'equipe_sistema'
        ]


class FormAlteraFuncionario(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = [
            'primeiro_nome',
            'ultimo_nome',
            'cpf',
            'data_nasc',
            'equipe_sistema',
            'password'
        ]


class FormVeterinario(forms.ModelForm):

    class Meta:
        model = Veterinario
        fields = [
            'primeiro_nome',
            'ultimo_nome',
            'cpf',
            'data_nasc',
            'equipe_sistema',
            'crmv',
            'estado_emissor',
            'id_funcionario'
        ]
