from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class AccountTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_permission_guest(self):
        response = self.client.get('/domains/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post('/domains/', {'url': 'https://habrahabr.ru'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_admin(self):
        admin = User(username='admin', password='1qa2ws3ed', is_staff=True, is_superuser=True)
        admin.save()

        self.client.force_authenticate(user=admin)
        response = self.client.post('/domains/', {'url': 'https://habrahabr.ru'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_admin3(self):
        admin3 = User(username='admin3', password='1qa2ws3ed', is_staff=True, is_superuser=True)
        admin3.save()

        self.client.force_authenticate(user=admin3)
        response = self.client.post('/domains/', {'url': 'https://habrahabr.ru'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/domains/', {'url': 'http://habrahabr.ru'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/domains/', {'url': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/domains/', {'url': 'noturl'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)