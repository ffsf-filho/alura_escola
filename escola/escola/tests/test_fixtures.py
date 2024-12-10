from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        '''
            Teste que verifica o carregamento da fixtures
        '''

        estudante = Estudante.objects.get(cpf = '58778739209')
        curso = Curso.objects.get(pk = 1)
        self.assertEqual(estudante.celular, '20 96544-9616')
        self.assertEqual(curso.codigo, 'POO')

