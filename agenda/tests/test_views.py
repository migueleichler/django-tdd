from django.test import TestCase, RequestFactory, Client
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
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('compromisso_novo'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compromisso_novo.html')

    def test_post(self):
        request = self.factory.post(reverse('compromisso_novo'),
                                    self.request_data)
        response = CreateCompromisso.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Compromisso.objects.filter(titulo=self.instance.titulo).exists()
        )
