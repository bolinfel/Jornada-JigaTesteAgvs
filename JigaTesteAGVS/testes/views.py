from typing import Any
from django.forms import BaseModelForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from testes.models import tbTestes, tbPropriedades
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import tbTestesForm
from django.http import JsonResponse

import random as rd

class TestesView(TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(CreateView):
    template_name = 'testeAutomatico.html'
    extra_context = {'Modelo':'CAN_IR',
                   'now':timezone.now(),
                   }
    model = tbTestes
    fields = ["FK_PLACA"]
    success_url = '/'

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
                RESULTADO=bool(rd.getrandbits(1)),  # Default result (can be changed later)
                TIPO_TESTE="AUT"  # Set TIPO_TESTE to "AUT"
            )
        
        # Redirect after processing
        return HttpResponseRedirect(self.success_url)


class TesteManualView(CreateView):
    template_name = 'testeManual.html'
    form_class = tbTestesForm
    success_url = '/testes'

    template_name = 'testeManual.html'
    form_class = tbTestesForm
    success_url = '/testes'

    def form_invalid(self, form):
        print("Formulário inválido:", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        fk_placa = form.cleaned_data['FK_PLACA']
        fk_propriedade = form.cleaned_data['FK_PROPRIEDADE']
        num_repeticoes = form.cleaned_data['num_repeticoes']  # Obtém o número de repetições do usuário

        print(f"Placa: {fk_placa}, Propriedade: {fk_propriedade}, Repetições: {num_repeticoes}")

        # Cria uma linha para cada repetição
        for _ in range(num_repeticoes):
            tbTestes.objects.create(
                DATA=timezone.now(),
                FK_PLACA=fk_placa,
                FK_PROPRIEDADE=fk_propriedade,
                RESULTADO=bool(rd.getrandbits(1)),  # Ajuste conforme necessário
                TIPO_TESTE="MAN"
            )

        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        # Check if the request is AJAX and contains fk_placa
        fk_placa = request.GET.get('fk_placa')
        
        if fk_placa:
            # Filter properties related to the selected board
            propriedades = tbPropriedades.objects.filter(FK_PLACA=fk_placa)
            propriedades_data = {prop.id: prop.DESCRICAO for prop in propriedades}
            return JsonResponse({'propriedades': propriedades_data})
        
        # If it's a standard GET request, render the form as usual
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        fk_placa = self.request.GET.get('fk_placa') or self.request.POST.get('FK_PLACA')

        if fk_placa:
            form.fields['FK_PROPRIEDADE'].queryset = tbPropriedades.objects.filter(FK_PLACA=fk_placa)
        else:
            form.fields['FK_PROPRIEDADE'].queryset = tbPropriedades.objects.none()
        
        return form

