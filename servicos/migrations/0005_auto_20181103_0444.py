# Generated by Django 2.0.6 on 2018-11-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_auto_20181103_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='descricao',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exame',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]