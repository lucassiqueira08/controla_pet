# Generated by Django 2.0.6 on 2018-10-20 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('url', models.CharField(max_length=50, verbose_name='Url')),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Item do Menu',
                'verbose_name_plural': 'Itens do Menu',
                'db_table': 'MENU',
            },
        ),
        migrations.CreateModel(
            name='MenuGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('url', models.CharField(max_length=50, verbose_name='Url')),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Grupo dos Itens do Menu',
                'verbose_name_plural': 'Grupos dos Itens do Menu',
                'db_table': 'MENU_GRUPO',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='id_menu_grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MenuGrupo'),
        ),
    ]
