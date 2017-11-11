from django.test import TestCase

from agenda.models import Compromisso
from model_mommy import mommy


class CompromissoModelTest(TestCase):

    def setUp(self):
        self.instance = mommy.make('Compromisso')

    def test_string_representation(self):
        self.assertEqual(str(self.instance), self.instance.titulo)

    def test_obrigatory_fields(self):
        created = Compromisso.objects.create(horario=self.instance.horario)
        self.assertTrue(isinstance(created, Compromisso))
