from django.db import models


class Menu(models.Model):

    descricao = models.TextField('Descrição')
    url = models.URLField(max_length=300)
    ordem = models.IntegerField('Ordem')
    id_menu_grupo = models.ForeignKey('MenuGrupo',
                                      on_delete=models.CASCADE)

    class Meta:
        app_label = 'core'
        db_table = 'MENU'
        verbose_name = 'Item do Menu'
        verbose_name_plural = 'Itens do Menu'

    def __str__(self):
        return self.descricao


class MenuGrupo(models.Model):

    descricao = models.TextField('Descrição')
    ordem = models.IntegerField('Ordem')

    class Meta:
        app_label = 'core'
        db_table = 'MENU_GRUPO'
        verbose_name = 'Grupo dos Itens do Menu'
        verbose_name_plural = 'Grupos dos Itens do Menu'

    def __str__(self):
        return self.descricao
