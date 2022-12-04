"""
test_admin.py
Tests Django admin site.
"""
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


# TODO: Improve all Admin test cases

class AdminTests(TestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            name='Test Name',
            surname='Test Surname'
        )
        self.client = Client()
        self.client.force_login(self.admin)

    def test_admin_main_screen(self):
        """Test if main screen loads successfully"""
        url = reverse('admin:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_list_screen(self):
        """Test users have listed on the screen successfully"""
        url = reverse('admin:dbo_user_changelist')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.surname)

    def test_create_new_user_screen(self):
        """Test create new user screen loads successfully"""
        url = reverse('admin:dbo_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_detail_screen(self):
        """Test user detail screen loads successfully"""
        url = reverse('admin:dbo_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
