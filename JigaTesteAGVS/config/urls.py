from django.urls import path
from config.views import NovaPlacaView, EditarPlacaView, EditarTipos

urlpatterns = [
    path('config/nova_placa', NovaPlacaView.as_view(), name='nova_placa'),
    path('config/editar_placa', EditarPlacaView.as_view(), name='editar_placa'),
]