from django.views.generic.base import TemplateView
from django.http import HttpResponse

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(TemplateView):
  template_name = 'testeAutomatico.html'
  extra_context = {'Modelo':'CAN_IR',
                   'statusTeste':'fazer'
                   }
  
  def teste_automatico_CAN(self):
      #inserir script do teste automatico
      self.extra_context['statusTeste'] = 'concluido'
  
  def get(self, request, *args, **kwargs):
        
    start_index = request.get_full_path_info().find('statusTeste=')

    if start_index == -1:
        status_value = 'fazer'
    # Move the start index to the end of 'statusTeste='
    start_index += len('statusTeste=')
    status_value = request.get_full_path_info()[start_index:]
    
    if status_value == "iniciado":
        self.teste_automatico_CAN()

    return super().get(self.request, *args, **kwargs)

  

class TesteManualView(TemplateView):
    template_name = 'testeManual.html'
    extra_context = {'Modelo':'CAN_IR',
                      'nEntradasDigitais':10,
                      'nSaidasDigitais':10,
                      'nEntradasAnalogicas':7,
                      'nSaidasAnalogicas':9
                    }