from django.views.generic.edit import CreateView

from .models import Compromisso


class CreateCompromisso(CreateView):
    model = Compromisso
    fields = ('titulo', 'horario', 'local', 'observacao')
