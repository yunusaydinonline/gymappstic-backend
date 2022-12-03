"""
test_models.py
Tests for DB models.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


def get_user_payload():
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }


class TestModels(TestCase):
    def test_create_user(self):
        """Test creating a user with username, email and password"""
        payload = get_user_payload()
        user = get_user_model().objects.create_user(**payload)

        self.assertEqual(user.username, payload['username'])
        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_apiuser)

        user = get_user_model().objects.get(id=user.id)
        self.assertTrue(user is not None)

    def test_create_user_without_username(self):
        """Test creating a user without username"""
        payload = get_user_payload()

        payload['username'] = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

        payload['username'] = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

    def test_create_user_without_email(self):
        """Test creating a user without email"""
        payload = get_user_payload()

        payload['email'] = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

        payload['email'] = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

    def test_create_user_without_password(self):
        """Test creating a user without password"""
        payload = get_user_payload()

        payload['password'] = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

        payload['password'] = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

    def test_create_user_with_email_normalized(self):
        """Test creating a user with normalized email"""
        emails = [
            ['testuser1', 'testuser1@example.COM', 'testuser1@example.com'],
            ['testuser2', 'TestUser2@eXamPle.cOm', 'TestUser2@example.com'],
            ['testuser3', 'TESTUSER3@EXAMPLE.COM', 'TESTUSER3@example.com'],
        ]

        for username, email, expected in emails:
            user = get_user_model().objects \
                .create_user(username, email, 'password123')

            self.assertEqual(user.email, expected)

    def test_create_superuser(self):
        """Test creating a super user with username, email and password."""

        payload = get_user_payload()
        user = get_user_model().objects.create_superuser(**payload)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_apiuser)

        user = get_user_model().objects.get(id=user.id)
        self.assertTrue(user is not None)

    def test_create_apiuser(self):
        """Test creating an API user with username, email and password"""

        payload = get_user_payload()
        user = get_user_model().objects.create_apiuser(**payload)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_apiuser)

        user = get_user_model().objects.get(id=user.id)
        self.assertTrue(user is not None)
