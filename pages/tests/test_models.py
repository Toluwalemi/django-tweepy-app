from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from pages.models import Tip, Link

now = datetime.now()


class TipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='Tolu', password='Test@12345')
        Tip.objects.create(user=user,
                           python_tip="Automate your docs creation workflow with Sphinx and Read the Docs",
                           posted_by="@python_tip",
                           is_published=True,
                           likes=3,
                           retweets=6,
                           timestamp=now.strftime("%m/%d/%Y %H:%M:%S"))

    def test_str_method(self):
        """Test that the model returns the correct string"""
        tip = tip = Tip.objects.get(id=1)
        expected_object_name = f'{tip.python_tip}'
        self.assertEqual(expected_object_name, str(tip))
        print("\n---------------------------------------------------------------------")


class LinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='Tolu', password='Test@12345')
        tip = Tip.objects.create(user=user,
                                 python_tip="Automate your docs creation workflow with Sphinx and Read the Docs",
                                 posted_by="@python_tip",
                                 is_published=True,
                                 likes=3,
                                 retweets=6,
                                 timestamp=now.strftime("%m/%d/%Y %H:%M:%S"))
        Link.objects.create(tip=tip,
                            tweet_link="https://twitter.com/python_tip/status/1347092859950780417")

    def test_str_method(self):
        """Test that the model returns the correct string"""
        link = Link.objects.get(id=1)
        expected_object_name = f'{link.tweet_link}'
        self.assertEqual(expected_object_name, str(link))
        print("\n---------------------------------------------------------------------")
