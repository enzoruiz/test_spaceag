from django.test import TestCase
from django.contrib.auth import get_user_model


class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        self.data_signup = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'testuser@email.com',
            'first_name': 'test',
            'last_name': 'user'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)

    def test_login_user_inactive(self):
        self.user.is_active = False
        self.user.save()

        response = self.client.post('/login', self.credentials, follow=True)

        self.assertFalse(response.context['user'].is_active)

    def test_signup(self):
        response = self.client.post('/signup', self.data_signup, follow=True)

        self.assertEqual(response.status_code, 200)
