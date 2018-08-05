from django.db import models

from cliente.models import Cliente, Animal, FichaAnimal
from usuarios.models import Funcionario


class Orcamento(models.Model):
    preco_final = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'servicos'
        db_table = 'ORCAMENTO'

    def __str__(self):
        return str(self.id)


class Atendimento(models.Model):
    
    observacao = models.CharField(max_length=100, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf_cliente')
    id_orcamento = models.ForeignKey(Orcamento, models.DO_NOTHING, db_column='id_orcamento', blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'ATENDIMENTO'

    def __str__(self):
        return str(self.id)


class ProcedimentoEstetico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    especie = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'servicos'
        db_table = 'PROCEDIMENTO_ESTETICO'

    def __str__(self):
        return self.nome


class TipoDiagnostico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'TIPO_DIAGNOSTICO'

    def __str__(self):
        return self.nome


class TipoExame(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'TIPO_EXAME'

    def __str__(self):
        return self.nome



class TipoProcedimento(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'TIPO_PROCEDIMENTO'

    def __str__(self):
        return self.nome



class ProcedimentoClinico(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    especie = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_tipo_proc = models.ForeignKey(TipoProcedimento, models.DO_NOTHING, db_column='id_tipo_proc')

    class Meta:
        app_label = 'servicos'
        db_table = 'PROCEDIMENTO_CLINICO'

    def __str__(self):
        return self.nome



class AtendimentoProcClinico(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_proc_clinico = models.ForeignKey(ProcedimentoClinico, models.DO_NOTHING, db_column='id_proc_clinico')

    class Meta:
        app_label = 'servicos'
        db_table = 'ATENDIMENTO_PROC_CLINICO'
        unique_together = (('id_atendimento', 'id_proc_clinico'),)

    def __str__(self):
        return 'Atendimento: ' + str(self.id_atendimento) + ' ' + 'Proc_Clinico:' + str(self.id_proc_clinico)



class AtendimentoProcEstetico(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_proc_estetico = models.ForeignKey(ProcedimentoEstetico, models.DO_NOTHING, db_column='id_proc_estetico')

    class Meta:
        app_label = 'servicos'
        db_table = 'ATENDIMENTO_PROC_ESTETICO'
        unique_together = (('id_atendimento', 'id_proc_estetico'),)

    def __str__(self):
        return 'Atendimento: ' + str(self.id_atendimento) + ' ' + 'Proc_Estetico: ' + str(self.id_proc_estetico)



class Autorizacao(models.Model):
    link_doc = models.CharField(unique=True, max_length=255, blank=True, null=True)
    id_proc_clinico = models.ForeignKey(ProcedimentoClinico, models.DO_NOTHING, db_column='id_proc_clinico')

    class Meta:
        app_label = 'servicos'
        db_table = 'AUTORIZACAO'

    def __str__(self):
        return str(self.id)



class Comissao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento')

    class Meta:
        app_label = 'servicos'
        db_table = 'COMISSAO'

    def __str__(self):
        return str(self.id)


class DiagnosticoAnimal(models.Model):
    descricao = models.CharField(max_length=500, blank=True, null=True)
    booleano = models.IntegerField(blank=True, null=True)
    id_tipo_diagnostico = models.ForeignKey(TipoDiagnostico, models.DO_NOTHING, db_column='id_tipo_diagnostico', blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'DIAGNOSTICO_ANIMAL'

    def __str__(self):
        return str(self.id)



class Estadia(models.Model):
    observacao = models.CharField(max_length=500, blank=True, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    data_solicitacao = models.DateField()
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf_cliente')

    class Meta:
        app_label = 'servicos'
        db_table = 'ESTADIA'

    def __str__(self):
        return str(self.id)



class Exame(models.Model):
    link_doc = models.CharField(unique=True,max_length=255)
    nome = models.CharField(max_length=100)
    data_realizacao = models.DateField(blank=True, null=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_tipo_exame = models.ForeignKey(TipoExame, models.DO_NOTHING, db_column='id_tipo_exame')

    class Meta:
        app_label = 'servicos'
        db_table = 'EXAME'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.nome)



class FeitoPor(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario')
    data_realizacao = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'FEITO_POR'
        app_label = 'servicos'
        unique_together = (('id_atendimento', 'id_funcionario'),)

    def __str__(self):
        return 'Atendimento: ' + str(self.id_atendimento) + ' ' + 'Funcionario: ' + str(self.id_funcionario)



class FichaDiagnostico(models.Model):
    id_diagnostico = models.IntegerField(primary_key=True)
    data_consulta = models.ForeignKey(FichaAnimal, models.DO_NOTHING, db_column='data_consulta', related_name='+')
    id_animal = models.ForeignKey(FichaAnimal, models.DO_NOTHING, db_column='id_animal', related_name='+')

    class Meta:
        app_label = 'servicos'
        db_table = 'FICHA_DIAGNOSTICO'
        unique_together = (('id_diagnostico', 'data_consulta', 'id_animal'),)

    def __str__(self):
        return str(self.id_animal) + ' - ' + 'Diagnostico: ' + str(self.id_diagnostico)



class TipoStatusAtendimento(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'TIPO_STATUS_ATENDIMENTO'

    def __str__(self):
        return self.nome



class TipoStatusEstadia(models.Model):
    nome_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'servicos'
        db_table = 'TIPO_STATUS_ESTADIA'

    def __str__(self):
        return self.nome_status




class StatusAtendimento(models.Model):
    id_atendimento = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='id_atendimento', primary_key=True)
    id_status = models.ForeignKey(TipoStatusAtendimento, models.DO_NOTHING, db_column='id_status')

    class Meta:
        db_table = 'STATUS_ATENDIMENTO'
        app_label = 'servicos'
        unique_together = (('id_atendimento', 'id_status'),)

    def __str__(self):
        return 'Atendimento: ' + str(self.id_atendimento) + ' ' + 'Status: ' + str(self.id_status)





class StatusEstadia(models.Model):
    id_estadia = models.ForeignKey(Estadia, models.DO_NOTHING, db_column='id_estadia', primary_key=True)
    id_status = models.ForeignKey(TipoStatusEstadia, models.DO_NOTHING, db_column='id_status')

    class Meta:
        db_table = 'STATUS_ESTADIA'
        app_label = 'servicos'
        unique_together = (('id_estadia', 'id_status'),)

    def __str__(self):
        return 'Estadia:' + str(self.id_estadia) + ' ' + 'Status: ' + str(self.id_status)
