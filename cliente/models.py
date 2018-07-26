from django.db import models


class TipoCliente(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'cliente'
        db_table = 'TIPO_CLIENTE'

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
        managed = False
        app_label = 'cliente'
        db_table = 'CLIENTE'

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
        managed = False
        app_label = 'cliente'
        db_table = 'ANIMAL'

    def __str__(self):
        return self.cpf_cliente + '-' + self.nome


class FichaAnimal(models.Model):
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING,
                                  db_column='id_animal', primary_key=True)
    data_consulta = models.DateField()
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'cliente'
        db_table = 'FICHA_ANIMAL'
        unique_together = (('id_animal', 'data_consulta'),)

    def __str__(self):
        return self.id


class TipoStatusAnimal(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'cliente'
        db_table = 'TIPO_STATUS_ANIMAL'

    def __str__(self):
        return self.id


class StatusAnimal(models.Model):

    id_status = models.ForeignKey('TipoStatusAnimal', models.DO_NOTHING,
                                  db_column='id_status', primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING,
                                  db_column='id_animal')

    class Meta:
        managed = False
        app_label = 'cliente'
        db_table = 'STATUS_ANIMAL'
        unique_together = (('id_status', 'id_animal'),)

    def __str__(self):
        return self.id_animal + ' ' + self.id_status


class TelefoneCliente(models.Model):

    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING,
                                    db_column='cpf_cliente', primary_key=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        managed = False
        app_label = 'cliente'
        db_table = 'TELEFONE_CLIENTE'
        unique_together = (('cpf_cliente', 'telefone'),)

    def __str__(self):
        return self.cpf_cliente + ' ' + self.telefone



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