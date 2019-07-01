from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.user1 = get_user_model().objects.create_user(
            email='test1@test.com',
            username='user1',
            password='password321',
        )

        self.user2 = get_user_model().objects.create_user(
            email='test2@test.com',
            username='user2',
            password='password321',
        )

        self.user3 = get_user_model().objects.create_user(
            email='test3@test.com',
            username='user3',
            password='password321',
        )

        self.token1, created = Token.objects.get_or_create(user=self.user1)
        self.token2, created = Token.objects.get_or_create(user=self.user2)
        self.token4, created = Token.objects.get_or_create(user=self.user3)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
