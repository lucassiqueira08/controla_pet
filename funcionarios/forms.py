from django import forms
from funcionarios.models import Funcionario, Veterinario


class FormFuncionario(forms.ModelForm):

    def save(self, commit=True):
        usuario = super(FormFuncionario, self).save(commit=False)
        usuario.set_password("123@mudar")
        if commit:
            usuario.save()
        return usuario


    class Meta:
        model = Funcionario
        fields = ['primeiro_nome', 'ultimo_nome', 'cpf', 'data_nasc', 'equipe_sistema', 'cargo']


class FormAlteraFuncionario(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['primeiro_nome', 'ultimo_nome', 'cpf', 'data_nasc', 'equipe_sistema', 'password', 'cargo']


class FormVeterinario(forms.ModelForm):

    class Meta:
        model = Veterinario
        fields = ['primeiro_nome', 'ultimo_nome', 'cpf', 'data_nasc', 'equipe_sistema', 'crm', 'estado_emissor']
