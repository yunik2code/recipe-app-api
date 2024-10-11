"""
Test For MOdels
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """
    Test MOdels
    """
    def test_create_user_with_email_successfull(self):

        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """
        Test if the user email is normalized
        """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@EXample.COM', 'test2@example.com'],
            ['Test3@Example.Com', 'Test3@example.com']
        ]
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email = email, password = 'sample123')
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """
        Testing that creating a user witjout email raises a value error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Test123')
    
    def test_create_superuser(self):
        """
        testing the creation of a superuser
        """
        user = get_user_model().objects.create_superuser(
            'test1@example.com', 'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)