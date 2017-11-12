from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy


class CompromissoViewTest(TestCase):

    def setUp(self):
        self.instance = mommy.make('Compromisso')
        self.request_data = {'titulo': self.instance.titulo,
                             'horario': self.instance.horario,
                             'local': self.instance.local,
                             'observacao': self.instance.observacao}
        self.client = Client()

    def test_create_compromisso(self):
        response = self.client.post(reverse('compromisso_novo'),
                                    self.request_data)

        self.assertEqual(response.status_code, 200)
