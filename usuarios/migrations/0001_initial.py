# Generated by Django 2.0.6 on 2018-10-20 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('primeiro_nome', models.CharField(max_length=50, verbose_name='Primeiro nome')),
                ('ultimo_nome', models.CharField(max_length=50, verbose_name='Último nome')),
                ('login', models.CharField(max_length=150, unique=True, verbose_name='Login')),
                ('is_staff', models.BooleanField(default=False, verbose_name='faz parte da equipe?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='é super usuario?')),
                ('situacao', models.BooleanField(default=True, verbose_name='Está ativo?')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'USER',
                'permissions': (('Admin', 'Permissao de adminstrador'), ('Usuario', 'Permissao de usuario')),
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'CARGO',
            },
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('equipe_sistema', models.BooleanField(verbose_name='tem acesso ao sistema?')),
                ('primeiro_nome', models.CharField(max_length=50, verbose_name='Primeiro nome')),
                ('ultimo_nome', models.CharField(max_length=50, verbose_name='Último nome')),
                ('crmv', models.CharField(max_length=50, unique=True, verbose_name='CRMV')),
                ('estado_emissor', models.CharField(max_length=2, verbose_name='Estado Emissor')),
            ],
            options={
                'verbose_name': 'Veterinário',
                'verbose_name_plural': 'Veterinários',
                'db_table': 'VETERINARIO',
            },
        ),
        migrations.CreateModel(
            name='CargoFuncionario',
            fields=[
                ('id_cargo', models.ForeignKey(db_column='id_cargo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuarios.Cargo')),
            ],
            options={
                'verbose_name': 'Cargo do Funcionário',
                'verbose_name_plural': 'Cargos dos Funcionários',
                'db_table': 'CARGO_FUNCIONARIO',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('equipe_sistema', models.BooleanField(verbose_name='tem acesso ao sistema?')),
                ('apelido', models.CharField(max_length=30, verbose_name='Apelido')),
                ('situacao_func', models.CharField(max_length=30, verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'db_table': 'FUNCIONARIO',
            },
            bases=('usuarios.user', models.Model),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='veterinario',
            name='id_funcionario',
            field=models.ForeignKey(db_column='id_funcionario', on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Funcionario'),
        ),
        migrations.AddField(
            model_name='cargofuncionario',
            name='id_func',
            field=models.ForeignKey(db_column='id_func', on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Funcionario'),
        ),
        migrations.AlterUniqueTogether(
            name='cargofuncionario',
            unique_together={('id_cargo', 'id_func')},
        ),
    ]