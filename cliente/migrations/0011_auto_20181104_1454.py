# Generated by Django 2.0.6 on 2018-11-04 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_auto_20181104_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusanimal',
            name='id_animal',
            field=models.ForeignKey(db_column='id_animal', on_delete=django.db.models.deletion.CASCADE, related_name='status_animal_animal', to='cliente.Animal'),
        ),
    ]
