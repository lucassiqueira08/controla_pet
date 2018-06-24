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

    def __str__(self):
        return self.primeiro_nome+' '+self.ultimo_nome

    def save(self, *args, **kwargs):
        self.login = str(self.primeiro_nome+'.'+self.ultimo_nome)
        super(User, self).save(*args, **kwargs)
