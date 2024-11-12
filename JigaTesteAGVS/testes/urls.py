from django.urls import path
from testes.views import TesteAutomaticoView, TesteManualView, TestesView, ListaPropriedadesView 

urlpatterns = [
    path('', TestesView.as_view(), name='testes'),
    path('automatico', TesteAutomaticoView.as_view(), name= 'testes.automatico'),
    path('manual', TesteManualView.as_view(), name= 'testes.manual'),
    path('placas', ListaPropriedadesView.as_view(), name='testes.lista'),
]