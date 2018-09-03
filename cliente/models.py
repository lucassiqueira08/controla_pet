from django.db import models


class TipoCliente(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'cliente'
        db_table = 'TIPO_CLIENTE'
        verbose_name = 'Tipo de Cliente'
        verbose_name_plural = 'Tipos de Clientes'

    def __str__(self):
        return self.nome


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
    id_tipo_cliente = models.ForeignKey('TipoCliente', models.DO_NOTHING,
                                        db_column='id_tipo_cliente')

    class Meta:
        app_label = 'cliente'
        db_table = 'CLIENTE'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
    

class Animal(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    cor = models.CharField(max_length=50, blank=True, null=True)
    datanasc = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    microchip = models.CharField(unique=True, max_length=50,
                                 blank=True, null=True)
    cpf_cliente = models.ForeignKey('Cliente', models.DO_NOTHING,
                                    db_column='cpf_cliente')

    class Meta:
        app_label = 'cliente'
        db_table = 'ANIMAL'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome


class FichaAnimal(models.Model):
    id = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING,
                                  db_column='id_animal')
    data_consulta = models.DateField(blank=True, null=False)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        app_label = 'cliente'
        db_table = 'FICHA_ANIMAL'
        verbose_name = 'Ficha do Animal'
        verbose_name_plural = 'Fichas dos Animais'

    def __str__(self):
        return 'Animal: ' + str(self.id_animal) + ' - ' + 'Data: ' + str(self.data_consulta)


class TipoStatusAnimal(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'cliente'
        db_table = 'TIPO_STATUS_ANIMAL'
        verbose_name = 'Tipo de Status do Animal'
        verbose_name_plural = 'Tipos de Status dos Animais'

    def __str__(self):
        return self.nome


class StatusAnimal(models.Model):

    id_status = models.ForeignKey(TipoStatusAnimal, models.DO_NOTHING,
                                  db_column='id_status', primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING,
                                  db_column='id_animal')

    class Meta:
        app_label = 'cliente'
        db_table = 'STATUS_ANIMAL'
        unique_together = (('id_status', 'id_animal'),)
        verbose_name = 'Status do Animal'
        verbose_name_plural = 'Status dos Animais'

    def __str__(self):
        return 'Animal:' + str(self.id_animal) + ' ' + 'Status:' + str(self.id_status)


class TelefoneCliente(models.Model):

    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING,
                                    db_column='cpf_cliente', primary_key=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        app_label = 'cliente'
        db_table = 'TELEFONE_CLIENTE'
        unique_together = (('cpf_cliente', 'telefone'),)
        verbose_name = 'Telefone do Cliente'
        verbose_name_plural = 'Telefones dos Clientes'

    def __str__(self):
        return 'Cliente:' + str(self.cpf_cliente) + ' ' + 'Telefone:' + str(self.telefone)


class Responde(models.Model):

    cpf_responsavel = models.ForeignKey(
        'Responsavel', models.DO_NOTHING,
        db_column='cpf_responsavel',
        primary_key=True
    )
    id_animal = models.ForeignKey(Animal,
                                  models.DO_NOTHING, db_column='id_animal')

    class Meta:
        db_table = 'RESPONDE'
        unique_together = (('cpf_responsavel', 'id_animal'),)
        verbose_name = 'Responsável por Animal (Responde)'
        verbose_name_plural = 'Responsáveis por Animais (Responde)'

    def __str__(self):
        return 'Responsavel:' + ' ' + str(self.cpf_responsavel) + ' - ' + 'Animal:' + ' ' + str(self.id_animal)


class Responsavel(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'RESPONSAVEL'
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome
