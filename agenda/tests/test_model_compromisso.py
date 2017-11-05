from django.test import TestCase

from model_mommy import mommy


class AgendaModelTest(TestCase):

    def setUp(self):
        self.test_instance = mommy.make('Compromisso')

    def test_string_representation(self):
        self.assertEqual(str(self.test_instance), self.test_instance.titulo)
