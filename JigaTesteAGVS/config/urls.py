from django.urls import path
from config.views import NovaPlacaView, EditarPlacaView

urlpatterns = [
    path('nova_placa/', NovaPlacaView.as_view(), name='nova_placa'),
    path('editar_placa/', EditarPlacaView.as_view(), name='editar_placa'),
]