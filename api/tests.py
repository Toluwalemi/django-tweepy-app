# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TipTests(APITestCase):

    def test_view_tips(self):
        """Test that all the objects are displayed"""
        url = reverse('api:list_view')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_tip(self):
        """Test that a user can create a new contribution"""
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='123456789')

        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {"daily_tip": "You can now post a python tip", "contributor": 1,
                "name_or_id": "Toluwalemi", "email": "test@user.com"}
        url = reverse('api:create_view')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_post_tip(self):
        """Test that a duplicate entry returns 400 bad request"""

        data = {"daily_tip": "You can now post a python tip", "contributor": 1,
                "name_or_id": "Toluwalemi", "email": "test@user.com"}
        url = reverse('api:create_view')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_post_tip(self):
        """Test that 400 is raised for an invalid contribution"""
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='123456789')

        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {
            "daily_tip": "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method"
                         "This is a daily tip. Make sure you add parenthesis to your print method",
            "contributor": 1,
            "name_or_id": "Toluwalemi", "email": "test@user.com"}
        url = reverse('api:create_view')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
