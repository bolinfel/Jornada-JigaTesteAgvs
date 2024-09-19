from django.views.generic.base import TemplateView

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(TemplateView):
  template_name = 'testeAutomatico.html'
  

class TesteManualView(TemplateView):
    template_name = 'testeManual.html'
    extra_context = {'Modelo':'CAN_IR',
                      'nEntradasDigitais':10,
                      'nSaidasDigitais':10,
                      'nEntradasAnalogicas':7,
                      'nSaidasAnalogicas':9
                    }