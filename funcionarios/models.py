from django.db import models

from usuarios.models import User


class FuncionarioAbstrato(models.Model):

    cpf = models.CharField('CPF', max_length=11, unique=True)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

    class Meta:
        abstract = True


class Funcionario(FuncionarioAbstrato, User):

    class Meta:
        dt_table = 'Funcionario'

    def __str__(self):
        return self.login


class Veterinario(FuncionarioAbstrato):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    crm = models.CharField('CRM', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)

    class Meta:
        dt_table = 'Veterinario'    

    def __str__(self):
        return self.primeiro_nome + self.ultimo_nome
