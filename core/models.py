from django.db import models


class Menu(models.Model):

    descricao = models.TextField('Descrição')
    url = models.URLField(max_length=300)
    ordem = models.IntegerField('Ordem')
    id_menu_grupo = models.ForeignKey('MenuGrupo',
                                      on_delete=models.CASCADE, )

    class Meta:
        app_label = 'core'
        db_table = 'MENU'


class MenuGrupo(models.Model):

    descricao = models.TextField('Descrição')
    ordem = models.IntegerField('Ordem')

    class Meta:
        app_label = 'core'
        db_table = 'MENU_GRUPO'
