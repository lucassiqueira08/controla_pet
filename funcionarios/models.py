from django.db import models
from usuarios.models import User
# Create your models here.

class FuncionarioAbstrato(User):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

class Funcionario(FuncionarioAbstrato):
    cargo = models.CharField('Cargo', max_length=30)

class Veterinario(FuncionarioAbstrato):
    crm = models.CharField('CRM', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)
    
