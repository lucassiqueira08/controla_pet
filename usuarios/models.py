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
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = (
            ("Admin", "Permissao de adminstrador"),
            ("Usuario", "Permissao de usuario"),
        )

    def __str__(self):
        return self.primeiro_nome+' '+self.ultimo_nome

    def save(self, *args, **kwargs):
        self.login = str(self.primeiro_nome+'.'+self.ultimo_nome)
        super(User, self).save(*args, **kwargs)


class FuncionarioAbstrato(models.Model):
    cpf = models.CharField('CPF', max_length=14, unique=True, null=False)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

    class Meta:
        abstract = True


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        app_label = 'usuarios'
        db_table = 'CARGO'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return str(self.id)


class Funcionario(FuncionarioAbstrato, User):
    apelido = models.CharField('Apelido', max_length=30)
    situacao_func = models.CharField('Situação', max_length=30, null=False)

    class Meta:
        app_label = 'usuarios'
        db_table = 'FUNCIONARIO'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.login


class Veterinario(FuncionarioAbstrato):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    crmv = models.CharField('CRMV', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)
    id_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE,
                                       related_name='veterinario_funcionario', db_column='id_funcionario')

    class Meta:
        app_label = 'usuarios'
        db_table = 'VETERINARIO'
        verbose_name = 'Veterinário'
        verbose_name_plural = 'Veterinários'

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome


class CargoFuncionario(models.Model):
    id_cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE,
                                    related_name='cargofuncionario_cargo', db_column='id_cargo',
                                    primary_key=True)
    id_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE,
                                related_name='cargofuncionario_funcionario',
                                db_column='id_func')

    class Meta:
        app_label = 'usuarios'
        db_table = 'CARGO_FUNCIONARIO'
        unique_together = (('id_cargo', 'id_func'),)
        verbose_name = 'Cargo do Funcionário'
        verbose_name_plural = 'Cargos dos Funcionários'

    def __str__(self):
        return 'Cargo: ' + str(self.id_cargo) + ' ' + 'Funcionario: ' + str(self.id_func)
