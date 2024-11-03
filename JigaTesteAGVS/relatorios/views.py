from django.views.generic import TemplateView, ListView
from testes.models import tbTestes
from time import timezone

class RelatoriosView(TemplateView):
    template_name = 'relatorios.html'

class ListaView(ListView):
    template_name = 'lista_testes.html'
    model = tbTestes
    paginate_by = 20

    context_object_name = 'testes'  # Nome que será usado para acessar os dados no template

    # Opcional: Ordene os resultados, por exemplo, pela data do teste
    queryset = tbTestes.objects.all().order_by('-DATA')
