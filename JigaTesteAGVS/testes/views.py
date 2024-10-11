from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from testes.models import tbTestes

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(CreateView):
    template_name = 'testeAutomatico.html'
    extra_context = {'Modelo':'CAN_IR',
                   'statusTeste':'fazer'
                   }
    model = tbTestes
    fields = ["FK_PLACA", "DATA"]
    success_url = ''


class TesteManualView(TemplateView):
    template_name = 'testeManual.html'
    extra_context = {'Modelo':'CAN_IR'}
    
