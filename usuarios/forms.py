from django import forms
from usuarios.models import User


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
