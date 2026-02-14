from django.urls import path


urlpatterns = [
    path('', views.listar_contatos, name='lista_contatos'),
]
