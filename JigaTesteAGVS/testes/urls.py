from django.urls import path
from testes.views import TesteAutomaticoView, TesteManualView, TestesView

urlpatterns = [
    path('', TestesView.as_view()),
    path('automatico', TesteAutomaticoView.as_view()),
    path('manual', TesteManualView.as_view()),
]