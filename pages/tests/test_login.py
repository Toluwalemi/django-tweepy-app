from django.test import TestCase
from django.contrib.sites.models import Site
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth import get_user_model

from config import settings


class TestLoginView(TestCase):

    def test_login(self):
        """Test that a user is logged in"""
        self.client = Client()
        self.username = "test@test.com"
        self.password = "password"
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)
        logged_in = self.client.login(username=self.username, password=self.password)
        self.assertTrue(logged_in)

    # def test_login(self):
    #     response = self.client.post(reverse(
    #         settings.LOGIN_URL), {"login": self.username, "password": self.password}
    #     )
    #     self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False)
