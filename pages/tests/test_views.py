import logging
import os

import tweepy
from django.test import TestCase

from pages.views import verify_twitter_credentials

logger = logging.getLogger(__name__)


class TweetTest(TestCase):
    def setUp(self):
        """Run once for every test method to setup clean data"""
        self.consumer_key = os.environ['TWITTER_API_KEY']
        self.consumer_secret = os.environ['TWITTER_SECRET_KEY']
        self.oauth_access_token = os.environ['TWITTER_ACCESS_TOKEN']
        self.oauth_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    def test_twitter_credentials(self):
        """Test that Twitter's API credentials are available"""
        self.assertTrue(os.environ['TWITTER_API_KEY'])
        self.assertTrue(os.environ['TWITTER_SECRET_KEY'])
        self.assertTrue(os.environ['TWITTER_ACCESS_TOKEN'])
        self.assertTrue(os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
        print("\n---------------------------------------------------------------------")

    def test_verify_credentials(self):
        """Verify the credentials with Tweepy"""
        auth = tweepy.OAuthHandler(str(self.consumer_key), str(self.consumer_secret))
        auth.set_access_token(str(self.oauth_access_token), str(self.oauth_access_token_secret))
        result = verify_twitter_credentials()
        self.assertTrue(result, 'API created')
        print("\n---------------------------------------------------------------------")

    def test_invalid_twitter_credentials(self):
        """Test that the Twiter credentials provided are invalid"""
        auth = tweepy.OAuthHandler("xF3VfjgH1FGQcuWOufvlhw", "xF3VfjgH1F4rfdGQcuWOufvlhw")
        auth.set_access_token("62259fE85Dq9oStl",
                              "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")
        # result = verify_twitter_credentials()
        # self.assertTrue(result, '"Error during authentication"')
        self.assertRaises(Exception, verify_twitter_credentials())
        print("\n---------------------------------------------------------------------")
