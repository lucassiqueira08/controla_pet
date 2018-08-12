from django.contrib import admin
from django.urls import path, include

from usuarios import urls as usuarios_urls
from core import urls as core_urls
from cliente import urls as cliente_urls


urlpatterns = [
    path('', include(core_urls)),
    path('admin/', admin.site.urls),
    path('usuario/', include(usuarios_urls)),
    path('cliente/', include(cliente_urls)),
]
