from django.views.generic.edit import CreateView

from .models import Compromisso


class CreateCompromisso(CreateView):
    model = Compromisso
    template_name = 'compromisso_novo.html'
    fields = ('titulo', 'horario', 'local', 'observacao')
