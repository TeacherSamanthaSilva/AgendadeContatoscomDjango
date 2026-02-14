from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # inclui as urls do app contatos
    path('', include('contatos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from ..contatos import views

urlpatterns = [
    path('', views.listar_contatos, name='lista_contatos'),
    path('novo/', views.criar_contato, name='criar_contato'),
    path('<int:id>/', views.detalhe_contato, name='detalhe_contato'),
    path('<int:id>/editar/', views.editar_contato, name='editar_contato'),
    path('<int:id>/excluir/', views.excluir_contato, name='excluir_contato'),
]

