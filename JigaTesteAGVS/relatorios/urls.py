from django.urls import path
from relatorios.views import RelatoriosView, ListaView, DashboardView, DetalhesView

urlpatterns = [
    path('', RelatoriosView.as_view(), name='relatorios'),
    path('lista', ListaView.as_view(), name='relatorios.lista'),
    path('dashboard', DashboardView.as_view(), name='relatorios.dashboard'),
    path('lista/<int:pk>/', DetalhesView.as_view(), name='relatorios.detalhes'),
]