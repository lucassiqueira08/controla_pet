# Generated by Django 2.0.6 on 2018-10-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]