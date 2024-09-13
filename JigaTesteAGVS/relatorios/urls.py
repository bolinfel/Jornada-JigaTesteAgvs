from django.urls import path
from relatorios.views import RelatoriosView

urlpatterns = [
    path('', RelatoriosView.as_view(), name='relatorios'),
]