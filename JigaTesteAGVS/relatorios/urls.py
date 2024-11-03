from django.urls import path
from relatorios.views import RelatoriosView, ListaView

urlpatterns = [
    path('', RelatoriosView.as_view(), name='relatorios'),
    path('lista', ListaView.as_view(), name='relatorios.lista'),
]