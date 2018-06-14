from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, login, password, **extra_fields):

        if not login:
            raise ValueError('Login não declarado')
        user = self.model(login=login, **extra_fields)
        user = set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(self, login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(self, login, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):

    login = models.CharField('Login', max_length=150, unique=True)
    first_name = models.CharField('Primeiro nome', max_length=50)
    last_name = models.CharField('Último nome', max_length=50)
    is_staff = models.BooleanField('faz parte da equipe?', default=False)
    is_superuser = models.BooleanField('é super usuario?', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.first_name+' '+self.last_name

# Create your models here.
