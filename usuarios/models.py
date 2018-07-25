from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)


class UserManager(BaseUserManager):

    def _create_user(self, password, **extra_fields):

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    login = models.CharField('Login', max_length=150, unique=True)
    is_staff = models.BooleanField('faz parte da equipe?', default=False)
    is_superuser = models.BooleanField('é super usuario?', default=False)
    situacao = models.BooleanField('Está ativo?', default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['primeiro_nome', 'ultimo_nome']
    USERNAME_FIELD = 'login'

    class Meta:
        app_label = 'usuarios'
        db_table = 'USER'

    def __str__(self):
        return self.primeiro_nome+' '+self.ultimo_nome

    def save(self, *args, **kwargs):
        self.login = str(self.primeiro_nome+'.'+self.ultimo_nome)
        super(User, self).save(*args, **kwargs)


class FuncionarioAbstrato(models.Model):

    cpf = models.CharField('CPF', max_length=11, unique=True)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

    class Meta:
        abstract = True


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        app_label = 'usuarios'
        db_table = 'CARGO'

        def __str__(self):
            return self.id


class Funcionario(FuncionarioAbstrato, User):

    class Meta:
        app_label = 'usuarios'
        db_table = 'FUNCIONARIO'

    def __str__(self):
        return self.login


class Veterinario(FuncionarioAbstrato):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    crm = models.CharField('CRM', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)

    class Meta:
        app_label = 'usuarios'
        db_table = 'VETERINARIO'

    def __str__(self):
        return self.primeiro_nome + self.ultimo_nome


class CargoFuncionario(models.Model):
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING,
                                 db_column='id_cargo', primary_key=True)
    id_func = models.ForeignKey('Funcionario', models.DO_NOTHING,
                                db_column='id_func')

    class Meta:
        managed = False
        app_label = 'usuarios'
        db_table = 'CARGO_FUNCIONARIO'
        unique_together = (('id_cargo', 'id_func'),)

    def __str__(self):
        return self.id_cargo + ' ' + self.id_func
