
from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    cor = models.CharField(max_length=50, blank=True, null=True)
    datanasc = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    microchip = models.CharField(unique=True, max_length=50, blank=True, null=True)
    cpf_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cpf_cliente')

    class Meta:
        managed = False
        db_table = 'ANIMAL'

    def __str__(self):
        return self.cpf_cliente + '-' + self.nome



class Atendimento(models.Model):
    observacao = models.CharField(max_length=100, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    cpf_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cpf_cliente')
    id_orcamento = models.ForeignKey('Orcamento', models.DO_NOTHING, db_column='id_orcamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATENDIMENTO'

    def __str__(self):
        return self.id




class AtendimentoProcClinico(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_proc_clinico = models.ForeignKey('ProcedimentoEstetico', models.DO_NOTHING, db_column='id_proc_clinico')

    class Meta:
        managed = False
        db_table = 'ATENDIMENTO_PROC_CLINICO'
        unique_together = (('id_atendimento', 'id_proc_clinico'),)

    def __str__(self):
        return self.id_atendimento + ' ' + self.id_proc_clinico




class AtendimentoProcEstetico(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_proc_estetico = models.ForeignKey('ProcedimentoEstetico', models.DO_NOTHING, db_column='id_proc_estetico')

    class Meta:
        managed = False
        db_table = 'ATENDIMENTO_PROC_ESTETICO'
        unique_together = (('id_atendimento', 'id_proc_estetico'),)

    def __str__(self):
        return self.id_atendimento + ' ' + self.id_proc_estetico




class Autorizacao(models.Model):
    link_doc = models.CharField(unique=True, max_length=500, blank=True, null=True)
    id_proc_clinico = models.ForeignKey('ProcedimentoClinico', models.DO_NOTHING, db_column='id_proc_clinico')

    class Meta:
        managed = False
        db_table = 'AUTORIZACAO'

    def __str__(self):
        return self.id



class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'CARGO'

    def __str__(self):
        return self.id



class CargoFuncionario(models.Model):
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo', primary_key=True)
    id_func = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_func')

    class Meta:
        managed = False
        db_table = 'CARGO_FUNCIONARIO'
        unique_together = (('id_cargo', 'id_func'),)

    def __str__(self):
        return self.id_cargo + ' ' + self.id_func




class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, blank=True, null=True)
    numero = models.SmallIntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    id_tipo_cliente = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='id_tipo_cliente')

    class Meta:
        managed = False
        db_table = 'CLIENTE'

    def __str__(self):
        return self.cpf


class Comissao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento')

    class Meta:
        managed = False
        db_table = 'COMISSAO'

    def __str__(self):
        return self.login



class DiagnosticoAnimal(models.Model):
    descricao = models.CharField(max_length=500, blank=True, null=True)
    booleano = models.IntegerField(blank=True, null=True)
    id_tipo_diagnostico = models.ForeignKey('TipoDiagnostico', models.DO_NOTHING, db_column='id_tipo_diagnostico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DIAGNOSTICO_ANIMAL'

    def __str__(self):
        return self.id



class Estadia(models.Model):
    observacao = models.CharField(max_length=500, blank=True, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    data_solicitacao = models.DateField()
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf_cliente')

    class Meta:
        managed = False
        db_table = 'ESTADIA'

    def __str__(self):
        return self.id



class Exame(models.Model):
    link_doc = models.CharField(unique=True, max_length=500)
    nome = models.CharField(max_length=100)
    data_realizacao = models.DateField(blank=True, null=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_tipo_exame = models.ForeignKey('TipoExame', models.DO_NOTHING, db_column='id_tipo_exame')

    class Meta:
        managed = False
        db_table = 'EXAME'

    def __str__(self):
        return self.id


class FeitoPor(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario')
    data_realizacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FEITO_POR'
        unique_together = (('id_atendimento', 'id_funcionario'),)

    def __str__(self):
        return self.id_atendimento + ' ' + self.id_funcionario



class FichaAnimal(models.Model):
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal', primary_key=True)
    data_consulta = models.DateField()
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FICHA_ANIMAL'
        unique_together = (('id_animal', 'data_consulta'),)

    def __str__(self):
        return self.id



class FichaDiagnostico(models.Model):
    id_diagnostico = models.IntegerField(primary_key=True)
    data_consulta = models.ForeignKey(FichaAnimal, models.DO_NOTHING, db_column='data_consulta')
    id_animal = models.ForeignKey(FichaAnimal, models.DO_NOTHING, db_column='id_animal')

    class Meta:
        managed = False
        db_table = 'FICHA_DIAGNOSTICO'
        unique_together = (('id_diagnostico', 'data_consulta', 'id_animal'),)

    def __str__(self):
        if __name__ == '__main__':
            return self.id_animal + ' ' + self.id_diagnostico



class Funcionario(models.Model):
    id = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    cpf = models.CharField(unique=True, max_length=11)
    data_nasc = models.DateField()
    equipe_sistema = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FUNCIONARIO'

    def __str__(self):
        return self.id


class Orcamento(models.Model):
    preco_final = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ORCAMENTO'

    def __str__(self):
        return self.id


class ProcedimentoClinico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    especie = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_tipo_proc = models.ForeignKey('TipoProcedimento', models.DO_NOTHING, db_column='id_tipo_proc')

    class Meta:
        managed = False
        db_table = 'PROCEDIMENTO_CLINICO'

    def __str__(self):
        return self.id



class ProcedimentoEstetico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    especie = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'PROCEDIMENTO_ESTETICO'

    def __str__(self):
        return self.id


class Responde(models.Model):
    cpf_responsavel = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='cpf_responsavel', primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')

    class Meta:
        managed = False
        db_table = 'RESPONDE'
        unique_together = (('cpf_responsavel', 'id_animal'),)

    def __str__(self):
        return self.cpf_responsavel + ' ' + self.id_animal


class Responsavel(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'RESPONSAVEL'

    def __str__(self):
        return self.cpf


class StatusAnimal(models.Model):
    id_status = models.ForeignKey('TipoStatusAnimal', models.DO_NOTHING, db_column='id_status', primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')

    class Meta:
        managed = False
        db_table = 'STATUS_ANIMAL'
        unique_together = (('id_status', 'id_animal'),)

    def __str__(self):
        return self.id_animal + ' ' + self.id_status


class StatusAtendimento(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_status = models.ForeignKey('TipoStatusAtendimento', models.DO_NOTHING, db_column='id_status')

    class Meta:
        managed = False
        db_table = 'STATUS_ATENDIMENTO'
        unique_together = (('id_atendimento', 'id_status'),)

    def __str__(self):
        return self.id_atendimento + ' ' + self.id_status



class StatusEstadia(models.Model):
    id_estadia = models.ForeignKey(Estadia, models.DO_NOTHING, db_column='id_estadia', primary_key=True)
    id_status = models.ForeignKey('TipoStatusEstadia', models.DO_NOTHING, db_column='id_status')

    class Meta:
        managed = False
        db_table = 'STATUS_ESTADIA'
        unique_together = (('id_estadia', 'id_status'),)

    def __str__(self):
        return self.id_estadia + ' ' + self.id_status



class TelefoneCliente(models.Model):
    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf_cliente', primary_key=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'TELEFONE_CLIENTE'
        unique_together = (('cpf_cliente', 'telefone'),)

    def __str__(self):
        return self.cpf_cliente + ' ' + self.telefone



class TipoCliente(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_CLIENTE'

    def __str__(self):
        return self.id


class TipoDiagnostico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_DIAGNOSTICO'

    def __str__(self):
        return self.id


class TipoExame(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_EXAME'

    def __str__(self):
        return self.id


class TipoProcedimento(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_PROCEDIMENTO'

    def __str__(self):
        return self.id


class TipoStatusAnimal(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_STATUS_ANIMAL'

    def __str__(self):
        return self.id


class TipoStatusAtendimento(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_STATUS_ATENDIMENTO'

    def __str__(self):
        return self.id



class TipoStatusEstadia(models.Model):
    nome_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_STATUS_ESTADIA'

    def __str__(self):
        return self.id


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    login = models.CharField(unique=True, max_length=150)
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    situacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'USER'

    def __str__(self):
        return self.login


class UserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'USER_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'USER_user_permissions'
        unique_together = (('user', 'permission'),)


class Veterinario(models.Model):
    cpf = models.CharField(unique=True, max_length=11)
    data_nasc = models.DateField()
    equipe_sistema = models.IntegerField()
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    crm = models.CharField(unique=True, max_length=50)
    estado_emissor = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'VETERINARIO'

    def __str__(self):
        return self.cpf


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
