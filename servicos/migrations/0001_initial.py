# Generated by Django 2.0.6 on 2018-10-20 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(blank=True, max_length=100, null=True)),
                ('data_solicitacao', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
                'db_table': 'ATENDIMENTO',
            },
        ),
        migrations.CreateModel(
            name='Autorizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_doc', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Autorização',
                'verbose_name_plural': 'Autorizações',
                'db_table': 'AUTORIZACAO',
            },
        ),
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Comissão',
                'verbose_name_plural': 'Comissões',
                'db_table': 'COMISSAO',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticoAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True)),
                ('booleano', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Diagnóstico do Animal',
                'verbose_name_plural': 'Diagnósticos dos Animais',
                'db_table': 'DIAGNOSTICO_ANIMAL',
            },
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(blank=True, max_length=500, null=True)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('data_solicitacao', models.DateField()),
                ('valor_diaria', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Estadia',
                'verbose_name_plural': 'Estadias',
                'db_table': 'ESTADIA',
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_doc', models.CharField(max_length=255, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_realizacao', models.DateField(blank=True, null=True)),
                ('id_animal', models.ForeignKey(db_column='id_animal', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Animal')),
            ],
            options={
                'verbose_name': 'Exame',
                'verbose_name_plural': 'Exames',
                'db_table': 'EXAME',
            },
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_final', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Orçamento',
                'verbose_name_plural': 'Orçamentos',
                'db_table': 'ORCAMENTO',
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoClinico',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('especie', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Procedimento Clinico',
                'verbose_name_plural': 'Procedimentos Clinicos',
                'db_table': 'PROCEDIMENTO_CLINICO',
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoEstetico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('especie', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Procedimento Estético',
                'verbose_name_plural': 'Procedimentos Estéticos',
                'db_table': 'PROCEDIMENTO_ESTETICO',
            },
        ),
        migrations.CreateModel(
            name='TipoDiagnostico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Diagnóstico',
                'verbose_name_plural': 'Tipos de Diagnósticos',
                'db_table': 'TIPO_DIAGNOSTICO',
            },
        ),
        migrations.CreateModel(
            name='TipoExame',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Exame',
                'verbose_name_plural': 'Tipos de Exames',
                'db_table': 'TIPO_EXAME',
            },
        ),
        migrations.CreateModel(
            name='TipoProcedimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Procedimento',
                'verbose_name_plural': 'Tipos de Procedimentos',
                'db_table': 'TIPO_PROCEDIMENTO',
            },
        ),
        migrations.CreateModel(
            name='TipoStatusAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Status do Atendimento',
                'verbose_name_plural': 'Tipos de Status dos Antendimentos',
                'db_table': 'TIPO_STATUS_ATENDIMENTO',
            },
        ),
        migrations.CreateModel(
            name='TipoStatusEstadia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Status da Estadia',
                'verbose_name_plural': 'Tipos de Status da Estadia',
                'db_table': 'TIPO_STATUS_ESTADIA',
            },
        ),
        migrations.CreateModel(
            name='AtendimentoProcClinico',
            fields=[
                ('id_atendimento', models.ForeignKey(db_column='id_atendimento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.Atendimento')),
            ],
            options={
                'verbose_name': 'Atendimento do Procedimento Clinico',
                'verbose_name_plural': 'Atendimentos dos Procedimentos Clínicos',
                'db_table': 'ATENDIMENTO_PROC_CLINICO',
            },
        ),
        migrations.CreateModel(
            name='AtendimentoProcEstetico',
            fields=[
                ('id_atendimento', models.ForeignKey(db_column='id_atendimento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.Atendimento')),
            ],
            options={
                'verbose_name': 'Atendimento do Procedimento Estético',
                'verbose_name_plural': 'Atendimentos dos Procedimentos Estéticos',
                'db_table': 'ATENDIMENTO_PROC_ESTETICO',
            },
        ),
        migrations.CreateModel(
            name='FeitoPor',
            fields=[
                ('id_atendimento', models.ForeignKey(db_column='id_atendimento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.Atendimento')),
                ('data_realizacao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Atendimento Feito por Funcionário (Feito Por)',
                'verbose_name_plural': 'Atendimentos Feitos por Funcionários (Feito Por)',
                'db_table': 'FEITO_POR',
            },
        ),
        migrations.CreateModel(
            name='FichaDiagnostico',
            fields=[
                ('id_diagnostico', models.ForeignKey(db_column='id_diagnostico', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.DiagnosticoAnimal')),
                ('id_ficha', models.ForeignKey(db_column='id_ficha', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.FichaAnimal')),
            ],
            options={
                'verbose_name': 'Ficha de Diagnóstico',
                'verbose_name_plural': 'Fichas de Diagnóstico',
                'db_table': 'FICHA_DIAGNOSTICO',
            },
        ),
        migrations.CreateModel(
            name='StatusAtendimento',
            fields=[
                ('id_atendimento', models.ForeignKey(db_column='id_atendimento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.Atendimento')),
                ('id_status', models.ForeignKey(db_column='id_status', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.TipoStatusAtendimento')),
            ],
            options={
                'verbose_name': 'Status do Atendimento',
                'verbose_name_plural': 'Status dos Atendimentos',
                'db_table': 'STATUS_ATENDIMENTO',
            },
        ),
        migrations.CreateModel(
            name='StatusEstadia',
            fields=[
                ('id_estadia', models.ForeignKey(db_column='id_estadia', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='servicos.Estadia')),
                ('id_status', models.ForeignKey(db_column='id_status', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.TipoStatusEstadia')),
            ],
            options={
                'verbose_name': 'Status da Estadia',
                'verbose_name_plural': 'Status das Estadias',
                'db_table': 'STATUS_ESTADIA',
            },
        ),
        migrations.AddField(
            model_name='procedimentoclinico',
            name='id_tipo_proc',
            field=models.ForeignKey(db_column='id_tipo_proc', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.TipoProcedimento'),
        ),
        migrations.AddField(
            model_name='exame',
            name='id_tipo_exame',
            field=models.ForeignKey(db_column='id_tipo_exame', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.TipoExame'),
        ),
        migrations.AddField(
            model_name='estadia',
            name='id_animal',
            field=models.ForeignKey(db_column='id_animal', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Animal'),
        ),
        migrations.AddField(
            model_name='diagnosticoanimal',
            name='id_tipo_diagnostico',
            field=models.ForeignKey(blank=True, db_column='id_tipo_diagnostico', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.TipoDiagnostico'),
        ),
        migrations.AddField(
            model_name='comissao',
            name='id_atendimento',
            field=models.ForeignKey(db_column='id_atendimento', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.Atendimento'),
        ),
        migrations.AddField(
            model_name='autorizacao',
            name='id_proc_clinico',
            field=models.ForeignKey(db_column='id_proc_clinico', on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.ProcedimentoClinico'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='cpf_cliente',
            field=models.ForeignKey(db_column='cpf_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Cliente'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='id_orcamento',
            field=models.ForeignKey(blank=True, db_column='id_orcamento', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.Orcamento'),
        ),
    ]