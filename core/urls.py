from django.urls import path

from .views import ViewIndex

urlpatterns = [
    path('index', ViewIndex.as_view(), name='index'),
    path('', ViewIndex.as_view(), name='index'),
]
