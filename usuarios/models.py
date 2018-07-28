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
    cpf = models.CharField('CPF', max_length=11, unique=True, null=False)
    data_nasc = models.DateField('Data de nascimento', null=False)
    equipe_sistema = models.BooleanField('tem acesso ao sistema?')

    class Meta:
        abstract = True


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        app_label = 'usuarios'
        db_table = 'CARGO'

    def __str__(self):
        return str(self.id)



class Funcionario(FuncionarioAbstrato, User):
    nome = models.CharField('Nome', max_length=50, null=False)
    apelido = models.CharField('Apelido', max_length=30)
    situacao_func = models.CharField('Situação', max_length=30, null=False)

    class Meta:
        app_label = 'usuarios'
        db_table = 'FUNCIONARIO'

    def __str__(self):
        return self.login


class Veterinario(FuncionarioAbstrato):

    primeiro_nome = models.CharField('Primeiro nome', max_length=50)
    ultimo_nome = models.CharField('Último nome', max_length=50)
    crmv = models.CharField('CRMV', max_length=50, unique=True)
    estado_emissor = models.CharField('Estado Emissor', max_length=2)
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario')

    class Meta:
        app_label = 'usuarios'
        db_table = 'VETERINARIO'

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome


class CargoFuncionario(models.Model):
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING,
                                 db_column='id_cargo', primary_key=True)
    id_func = models.ForeignKey('Funcionario', models.DO_NOTHING,
                                db_column='id_func')

    class Meta:
        app_label = 'usuarios'
        db_table = 'CARGO_FUNCIONARIO'
        unique_together = (('id_cargo', 'id_func'),)

    def __str__(self):
        return 'Cargo: ' + str(self.id_cargo) + ' ' + 'Funcionario: ' + str(self.id_func)




# class UserGroups(models.Model):
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     group = models.ForeignKey('AuthGroup', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'USER_groups'
#         unique_together = (('user', 'group'),)
#
#
# class UserUserPermissions(models.Model):
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'USER_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(User, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'

