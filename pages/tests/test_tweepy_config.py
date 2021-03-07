import os

import tweepy
from django.test import TestCase

from pages.helpers.tweepy_config import create_api, check_rate_limit


class TweetTest(TestCase):

    def test_twitter_credentials(self):
        """Test that Twitter's API credentials are available in environment"""
        self.assertTrue(os.environ['TWITTER_API_KEY'])
        self.assertTrue(os.environ['TWITTER_SECRET_KEY'])
        self.assertTrue(os.environ['TWITTER_ACCESS_TOKEN'])
        self.assertTrue(os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
        print("\n---------------------------------------------------------------------")

    def test_verify_credentials(self):
        """Verify the credentials with Tweepy"""
        result = create_api()
        self.assertTrue(result, 'API created')
        print("\n---------------------------------------------------------------------")

    def test_invalid_twitter_credentials(self):
        """Test that the Twiter credentials provided are invalid"""
        auth = tweepy.OAuthHandler("xF3VfjgH1FGQcuWOufvlhw", "xF3VfjgH1F4rfdGQcuWOufvlhw")
        auth.set_access_token("62259fE85Dq9oStl",
                              "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")
        self.assertRaises(Exception, create_api())
        print("\n---------------------------------------------------------------------")

    def test_check_rate_limit(self):
        func = check_rate_limit()
        self.assertEqual(func, 200)
