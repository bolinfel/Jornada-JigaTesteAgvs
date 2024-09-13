from django.urls import path
from testes.views import TesteAutomaticoView, TesteManualView, TestesView

urlpatterns = [
    path('', TestesView.as_view(), name='testes'),
    path('automatico', TesteAutomaticoView.as_view(), name= 'testes.automatico'),
    path('manual', TesteManualView.as_view(), name= 'testes.manual'),
]