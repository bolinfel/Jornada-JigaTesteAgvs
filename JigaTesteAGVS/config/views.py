from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from testes.models import tbPlacas, tbPropriedades, tbTipos
from django.core.serializers.json import DjangoJSONEncoder
import json

class NovaPlacaView(TemplateView):
    pass

class EditarPlacaView(TemplateView):
    template_name = "editar_propriedades.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        placas = tbPlacas.objects.all()
        tipos = tbTipos.objects.all()

        placa_id = self.request.GET.get('placa_id')
        selected_placa = None
        propriedades = []

        if placa_id:
            selected_placa = get_object_or_404(tbPlacas, id=placa_id)
            propriedades = tbPropriedades.objects.filter(FK_PLACA=selected_placa)

        context.update({
            "placas": placas,
            "tipos": tipos,
            "selected_placa": selected_placa,
            "propriedades": propriedades,
            "tipos_json": json.dumps(list(tipos.values("id", "NOME")), cls=DjangoJSONEncoder),
        })
        return context

    def post(self, request, *args, **kwargs):
        placa_id = request.POST.get('placa_id')
        selected_placa = get_object_or_404(tbPlacas, id=placa_id)
        tbPropriedades.objects.filter(FK_PLACA=selected_placa).delete()

        propriedades_data = zip(
            request.POST.getlist('tipo_id'),
            request.POST.getlist('porta'),
            request.POST.getlist('descricao'),
        )

        for tipo_id, porta, descricao in propriedades_data:
            if tipo_id and porta and descricao:
                tbPropriedades.objects.create(
                    FK_PLACA=selected_placa,
                    FK_TIPO_id=tipo_id,
                    PORTA=porta,
                    DESCRICAO=descricao,
                )

        return JsonResponse({'success': True})
