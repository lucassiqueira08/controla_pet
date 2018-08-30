from django.urls import path

from .views import ViewIndex
from .views import ViewIndexBemVindo

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path('', ViewIndexBemVindo.as_view(), name='index_bemvindo'),
]
