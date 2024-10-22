from typing import Any
from django.forms import BaseModelForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from testes.models import tbTestes, tbPropriedades
from django.utils import timezone
from django.http import HttpResponseRedirect

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(CreateView):
    template_name = 'testeAutomatico.html'
    extra_context = {'Modelo':'CAN_IR',
                   'statusTeste':'fazer'
                   }
    model = tbTestes
    fields = ["FK_PLACA"]
    success_url = 'testes'

    def form_valid(self, form):
        # Get the selected FK_PLACA from the form
        fk_placa = form.cleaned_data['FK_PLACA']
        
        # Get all properties related to this board
        propriedades = tbPropriedades.objects.filter(FK_PLACA=fk_placa)
        
        # Create a test record for each property
        for propriedade in propriedades:
            # COLOCAR AQUI O TESTE AUTOMATICO
            tbTestes.objects.create(
                DATA=timezone.now(),
                FK_PLACA=fk_placa,
                FK_PROPRIEDADE=propriedade,
                RESULTADO=False,  # Default result (can be changed later)
                TIPO_TESTE="AUT"  # Set TIPO_TESTE to "AUT"
            )
        
        # Redirect after processing
        return HttpResponseRedirect(self.success_url)


class TesteManualView(CreateView):
    template_name = 'testeManual.html'
    extra_context = {'Modelo':'CAN_IR'}
    model = tbTestes
    fields = ["FK_PLACA", "DATA", "TIPO_TESTE","FK_PROPRIEDADE",]
    success_url = 'testes'
