from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        
        self.estudante_01 = Estudante.objects.create(
            nome = 'TesteEstudanet UM',
            email = 'testeestudante01@gmail.com',
            cpf = '68224431002',
            data_nascimento = '2024-01-02',
            celular = '86 99999-9999'
        )

        self.estudante_02 = Estudante.objects.create(
            nome = 'TesteEstudanet DOIS',
            email = 'testeestudante02@gmail.com',
            cpf = '70261486055',
            data_nascimento = '2024-01-02',
            celular = '86 99999-9999'            
        )

    def test_requisicao_get_para_listar_estundantes(self):
        '''
            Teste de requisição GET
        '''
        response = self.client.get(self.url) #/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estundantes(self):
        '''
            Teste de requisição GET para um estudante
        '''
        response = self.client.get(self.url + '1/') #/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        #print(dados_estudante_serializados)
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        '''
            Teste de requisição POST para um estudante
        '''
        dados = {
            'nome': 'Teste',
            'email': 'teste@gmail.com',
            'cpf': '82271917034',
            'data_nascimento': '2003-05-04',
            'celular': '11 91234-4586'
        }

        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_um_estudante(self):
        '''
            Teste de requisição DELETE um estudante
        '''
        response = self.client.delete(f'{self.url}2/') #/estudante/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_requisicao_put_para_atualizar_um_estudante(self):
        '''
            Teste de requisição PUT para um estudante
        '''

        dados = {
            'nome': 'teste',
            'email': 'testeput@gmail.com',
            'cpf': '42370866071',
            'data_nascimento': '2003-05-09',
            'celular' : '11 98888-6666'
        }

        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    