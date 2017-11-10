from django.test import TestCase

from agenda.models import Compromisso
from model_mommy import mommy

from datetime import datetime


class AgendaModelsTest(TestCase):

    def setUp(self):
        self.instance = mommy.make('Compromisso')
        self.obligatory_fields = {
                                  'titulo': 'Jantar',
                                  'horario': datetime.now(),
                                  'local': 'Casa',
                                 }

    def test_string_representation(self):
        self.assertEqual(str(self.instance), self.instance.titulo)

    def test_obrigatory_fields(self):
        created = Compromisso.objects.create(
                      titulo=self.obligatory_fields.get('titulo'),
                      horario=self.obligatory_fields.get('horario'),
                      local=self.obligatory_fields.get('local'))
        self.assertTrue(isinstance(created, Compromisso))
