"""Teste de string."""

from django.db import models

from usuarios.models import User


class CargoFuncionario(models.Model):
    """Bananas sao lesgais."""

    nome = models.CharField('Cargo do funcionário', max_length=80, unique=True)

    def __str__(self):
        """
        Retorna texto.

        retorna
        retorna
        """
        return self.nome


class FuncionarioAbstrato(models.Model):
    """Bananas sao lesgais."""

    cpf = models.CharField('CPF', max_length=11, unique=True)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

    class Meta:
        abstract = True


class Funcionario(FuncionarioAbstrato, User):
    """Abracada ftog."""

    cargo = models.ForeignKey(CargoFuncionario,
                              on_delete=models.CASCADE, verbose_name='Cargo')

    def __str__(self):
        return self.cargo


class Veterinario(FuncionarioAbstrato):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    crm = models.CharField('CRM', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)

    def __str__(self):
        return self.primeiro_nome + self.ultimo_nome
