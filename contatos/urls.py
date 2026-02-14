from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contatos, name='lista_contatos'),
]
