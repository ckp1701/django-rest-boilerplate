from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse

from app.core.tests import BaseTestCase


class UserRegisterTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.registration_url = reverse('rest_register')

    def test_correct_register(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test4@test.pl',
                                        'password1': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'password2': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'username': 'user4'
                                    })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('key', response.data)

    def test_missing_email(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': '',
                                        'password1': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'password2': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'username': 'user4'
                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_username(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test4@test.pl',
                                        'password1': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'password2': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'username': ''
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_different_passwords(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test5@test.pl',
                                        'password1': "7f88sd6f7sdf686sdf67s8d6fdf6aaaaaaa",
                                        'password2': "7f88sd6f7sdf686sdf67s8d6fdf6",
                                        'username': 'test5'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_weak_password(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test5@test.pl',
                                        'password1': "1234",
                                        'password2': "1234",
                                        'username': 'test5'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # password too similar to email/username

        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test6@test.pl',
                                        'password1': "test6",
                                        'password2': "test6",
                                        'username': 'test6'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_password_input(self):
        response = self.client.post(self.registration_url,
                                    {
                                        'email': 'test7@test.pl',
                                        'password1': "",
                                        'password2': "",
                                        'username': 'test7'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.login_url = reverse('rest_login')
        self.user4 = get_user_model().objects.create_user(
            email='test4@test.com',
            username='user4',
            password='password321',
        )

    def test_correct_login(self):
        response = self.client.post(self.login_url,
                                    {
                                        'email': 'test4@test.com',
                                        'password': 'password321',
                                        'username': 'user4'
                                    })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('key', response.data)

    def test_invalid_password(self):
        response = self.client.post(self.login_url,
                                    {
                                        'email': 'test4@test.com',
                                        'password': 'password',
                                        'username': 'user4'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('key', response.data)

    def test_invalid_username_email(self):
        response = self.client.post(self.login_url,
                                    {
                                        'email': 'test4bad@test.com',
                                        'password': 'password321',
                                        'username': 'user3333'
                                    })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('key', response.data)


class ConfigurationViewTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.list_url = reverse('configurations-list')
        self.detail_url = reverse('configurations-detail', kwargs={'pk': 1})

    def test_get_configuration(self):
        response = self.client.get(self.list_url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_configuration(self):
        response = self.client.patch(self.detail_url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
