from django.views.generic import TemplateView

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(TemplateView):
  template_name = 'testeAutomatico.html'

class TesteManualView(TemplateView):
    template_name = 'testeManual.html'