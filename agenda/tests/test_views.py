from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse


from model_mommy import mommy
from agenda.views import CreateCompromisso
from agenda.models import Compromisso


class CompromissoViewTest(TestCase):

    def setUp(self):
        self.instance = mommy.make('Compromisso')
        self.request_data = {'titulo': self.instance.titulo,
                             'horario': self.instance.horario,
                             'local': self.instance.local,
                             'observacao': self.instance.observacao}
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('compromisso_novo'))
        response = CreateCompromisso.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = self.factory.post(reverse('compromisso_novo'), self.request_data)

        response = CreateCompromisso.as_view()(request)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Compromisso.objects.last().titulo, self.instance.titulo)
