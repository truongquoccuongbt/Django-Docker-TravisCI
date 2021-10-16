from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        email = 'cuong@gmail.com'
        password = '123456'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalize(self):
        email = 'cuong@GMAIL.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_create_user_supperuser(self):
        email = 'cuong@GMAIL.com'
        password = '123456'

        user = get_user_model().objects.create_supper_admin(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_validation_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')
