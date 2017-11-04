from django.test import TestCase

from model_mommy import mommy


class AgendaModelTest(TestCase):

    def test_models_creation(self):
        compromisso = mommy.make('Compromisso')
        self.assertTrue(isinstance(compromisso, Compromisso))
