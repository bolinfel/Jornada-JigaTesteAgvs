from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View
from testes.models import tbTestes, tbPropriedades, tbOperacoes, tbPlacas
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .forms import tbTestesForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
import random as rd

class TestesView(LoginRequiredMixin, TemplateView):
   template_name = 'testes.html'

class TesteAutomaticoView(LoginRequiredMixin, CreateView):
    login_url = "/user/login/"
    template_name = 'testeAutomatico.html'
    extra_context = {'Modelo':'CAN_IR',
                   'now':timezone.now(),
                   }
    model = tbTestes
    fields = ["FK_PLACA"]
    success_url = '/relatorios/lista'

    def form_valid(self, form):
        # Get the selected FK_PLACA from the form
        fk_placa = form.cleaned_data['FK_PLACA']
        
        # Get all properties related to this board
        propriedades = tbPropriedades.objects.filter(FK_PLACA=fk_placa)
        
        operacao = tbOperacoes.objects.create(
            USUARIO=self.request.user,
            TIPO_TESTE="AUT",
            DATA=timezone.now()
        )

        # Create a test record for each property
        for propriedade in propriedades:
            # COLOCAR AQUI O TESTE AUTOMATICO
            tbTestes.objects.create(
                DATA=timezone.now(),
                FK_PLACA=fk_placa,
                FK_OPERACAO=operacao,
                FK_PROPRIEDADE=propriedade,
                RESULTADO=bool(rd.getrandbits(1)),  # Default result (can be changed later)
                TIPO_TESTE="AUT"  # Set TIPO_TESTE to "AUT"
            )
        
        # Redirect after processing
        return HttpResponseRedirect(self.success_url)

class TesteManualView(LoginRequiredMixin, CreateView):
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

        operacao = tbOperacoes.objects.create(
            USUARIO=self.request.user,
            TIPO_TESTE="MAN",
            DATA=timezone.now()
        )

        # Cria uma linha para cada repetição
        for _ in range(num_repeticoes):
            tbTestes.objects.create(
                DATA=timezone.now(),
                FK_OPERACAO=operacao,
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

class ListaPropriedadesView(LoginRequiredMixin, TemplateView):
    template_name = 'listaPropriedades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all boards and selected board
        placa_id = self.request.GET.get('placa_id')
        context['placas'] = tbPlacas.objects.all()
        
        if placa_id:
            placa = get_object_or_404(tbPlacas, id=placa_id)
            context['selected_placa'] = placa
            
            # Get properties for the selected board and add the latest test info for each
            propriedades = tbPropriedades.objects.filter(FK_PLACA=placa).annotate(
                latest_test_date=Max('tbtestes__DATA')
            )

            properties_with_latest_test = []

            # Check if properties are being retrieved correctly
            if not propriedades:
                print("No properties found for the selected board.")
            
            for propriedade in propriedades:
                # Retrieve the latest test for each property
                latest_test = tbTestes.objects.filter(FK_PLACA=placa, FK_PROPRIEDADE=propriedade).order_by('-DATA').first()
                properties_with_latest_test.append({
                    'propriedade': propriedade,
                    'latest_test_date': latest_test.DATA if latest_test else None,
                    'latest_test_result': latest_test.RESULTADO if latest_test else None
                })

            context['properties_with_latest_test'] = properties_with_latest_test
        else:
            context['properties_with_latest_test'] = []

        return context



    def post(self, request, *args, **kwargs):
        # Handle single test execution when button is clicked
        propriedade_id = request.POST.get('propriedade_id')
        placa_id = request.POST.get('placa_id')

        if propriedade_id:
            propriedade = get_object_or_404(tbPropriedades, id=propriedade_id)
            operacao = tbOperacoes.objects.create(
                USUARIO=request.user,
                TIPO_TESTE="MAN",
                DATA=timezone.now()
            )

            tbTestes.objects.create(
                DATA=timezone.now(),
                FK_PLACA=propriedade.FK_PLACA,
                FK_PROPRIEDADE=propriedade,
                FK_OPERACAO=operacao,
                RESULTADO=bool(rd.getrandbits(1)),  # Default result (adjust based on your logic)
                TIPO_TESTE="Manual"
            )

        # Redirect back to the page with the selected board's properties
        return redirect(f"{self.request.path}?placa_id={placa_id}")
