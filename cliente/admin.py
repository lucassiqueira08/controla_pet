from django.contrib import admin
from cliente.models import TipoCliente, Cliente, Animal, FichaAnimal, TipoStatusAnimal, StatusAnimal, \
    TelefoneCliente, Responde, Responsavel


admin.site.register(TipoCliente)
admin.site.register(Cliente)
admin.site.register(Animal)
admin.site.register(FichaAnimal)
admin.site.register(TipoStatusAnimal)
admin.site.register(StatusAnimal)
admin.site.register(TelefoneCliente)
admin.site.register(Responde)
admin.site.register(Responsavel)


