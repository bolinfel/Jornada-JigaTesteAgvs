from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from testes.models import tbPlacas, tbPropriedades, tbTipos
from django.forms.models import modelformset_factory

class NovaPlacaView(TemplateView):
    pass

class EditarPlacaView(View):
    template_name = 'editar_propriedades.html'

    def get(self, request):
        # Obter todas as placas para o seletor
        placas = tbPlacas.objects.all()

        # Verificar se uma placa foi selecionada
        placa_id = request.GET.get('placa_id')
        selected_placa = None
        propriedades = None
        tipos = tbTipos.objects.all()

        if placa_id:
            selected_placa = get_object_or_404(tbPlacas, id=placa_id)
            propriedades = tbPropriedades.objects.filter(FK_PLACA=selected_placa)

        return render(request, self.template_name, {
            'placas': placas,
            'selected_placa': selected_placa,
            'propriedades': propriedades,
            'tipos': tipos,
        })

    def post(self, request):
        # Atualizar as propriedades da placa
        placa_id = request.POST.get('placa_id')
        selected_placa = get_object_or_404(tbPlacas, id=placa_id)

        # Processar as propriedades enviadas
        propriedades_data = zip(
            request.POST.getlist('propriedade_id'),
            request.POST.getlist('tipo_id'),
            request.POST.getlist('porta'),
            request.POST.getlist('descricao'),
        )

        for propriedade_id, tipo_id, porta, descricao in propriedades_data:
            if propriedade_id:
                # Atualizar a propriedade existente
                propriedade = get_object_or_404(tbPropriedades, id=propriedade_id)
                propriedade.FK_TIPO_id = tipo_id
                propriedade.PORTA = porta
                propriedade.DESCRICAO = descricao
                propriedade.save()

        return redirect('editar_propriedades')  # Redirecionar para a mesma página
