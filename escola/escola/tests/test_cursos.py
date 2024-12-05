from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)