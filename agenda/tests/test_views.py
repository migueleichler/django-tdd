from django.test import TestCase, RequestFactory

from agenda.views import CreateCompromisso
from model_mommy import mommy


class CompromissoViewTest(TestCase):

    def setUp(self):
        self.instance = mommy.make('Compromisso')
        self.factory = RequestFactory()

    def test_create_compromisso(self):
        request = self.factory.post('/compromisso/novo/',
                                    {'titulo': self.instance.titulo,
                                     'horario': self.instance.horario,
                                     'local': self.instance.local,
                                     'observacao': self.instance.observacao})
        response = CreateCompromisso.as_view()(request)

        self.assertEqual(response.status_code, 200)
