from django.views.generic import TemplateView, ListView, DetailView
from testes.models import tbTestes, tbPlacas, tbPropriedades, tbTipos
from django.db.models import Count, Q
from time import timezone
from django.shortcuts import render

class RelatoriosView(TemplateView):
    template_name = 'relatorios.html'

class ListaView(ListView):
    template_name = 'lista_testes.html'
    model = tbTestes

    context_object_name = 'testes'  # Nome que será usado para acessar os dados no template

    # Opcional: Ordene os resultados, por exemplo, pela data do teste
    queryset = tbTestes.objects.all().order_by('-DATA')

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fk_placa_id = self.request.GET.get('fk_placa')  # Get selected board ID from URL query string

        # Set the selected board ID to be used in the template
        context['selected_fk_placa'] = fk_placa_id

        # Filter tests by the selected board and calculate success rates
        if fk_placa_id:
            properties = tbPropriedades.objects.filter(FK_PLACA_id=fk_placa_id)
            success_data = []

            for prop in properties:
                total_tests = tbTestes.objects.filter(FK_PROPRIEDADE=prop).count()
                successful_tests = tbTestes.objects.filter(FK_PROPRIEDADE=prop, RESULTADO=True).count()
                success_rate = (successful_tests / total_tests) * 100 if total_tests > 0 else 0
                success_data.append({
                    'property': prop.DESCRICAO,
                    'success_rate': success_rate
                })

            context['success_data'] = success_data

        # Fetch all boards for the dropdown selection
        context['boards'] = tbPlacas.objects.all()
        return context


class DetalhesView(DetailView):
    model = tbTestes
    template_name = 'detalhes.html'
    context_object_name = 'teste'